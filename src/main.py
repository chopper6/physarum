import networkx as nx, random as rd, numpy as np
import init, update, stats, output, plot


def run(num_iters, num_reps, output_dirr, Qfunction='default', gamma=2, num_nodes=200, pr_edge=.4, verbose = False):

    accuracy, convergence_iterations = 0, 0

    for rep in range(num_reps):

        net, Adj ,L, R, D, Q, B, P = init.net_and_matrices(num_nodes=num_nodes, pr_edge = pr_edge, init_type='random')
        output.init_output(output_dirr)

        final_iter = num_iters
        for i in range(num_iters):
            R, P, Q, D, converged = update.update_net(Adj,L, R, D, Q, B, P, Qfunction=Qfunction, gamma=gamma)
            #phys_path, nx_path = stats.extract_shortest_path(net, D, L, B)
            #true_pos, false_pos, true_neg, false_neg, correct = stats.score(phys_path, nx_path, net, output_dirr + "/accuracy.csv")
            #output.write_confusion(true_pos, false_pos, true_neg, false_neg, i, output_dirr)
            if converged:
                final_iter = i
                break

        phys_path, nx_path = stats.extract_shortest_path(D, L, B)
        if verbose: print("Actual shortest path: " + str(nx_path) + ", Physarum shortest path:" + str(phys_path))
        true_pos, false_pos, true_neg, false_neg, correct = stats.score(phys_path, nx_path, net, output_dirr + "/accuracy.csv")
        if correct:
            accuracy += 1
            convergence_iterations += final_iter

    convergence_iterations /= accuracy #accuracy is just #times converged right now
    accuracy /= num_reps
    print("Accuracy = " + str(accuracy))
    print("Mean convergence iterations = " + str(convergence_iterations))
    #plot.accuracy(output_dirr)


def Qfn_experiment(gammas, output_dirr):

    num_iters, num_reps = 200,20
    num_nodes, pr_edge = 80, .4

    for gamma in gammas:
        print("\n\n##########################################   GAMMA = "  +str(gamma) + "   ##########################################\n")
        run(num_iters, num_reps, output_dirr, Qfunction='alt', gamma=gamma, num_nodes=num_nodes, pr_edge=pr_edge)

    print("\n\n##########################################   CONTROL   ##########################################\n")
    run(num_iters, num_reps, output_dirr, num_nodes=num_nodes, pr_edge=pr_edge)

if __name__ == "__main__":

    #TODO: poor convergence, figs for results

    output_dirr = "C:/Users/Crbn/Documents/Code/physarum/test"
    #This is my local path and needs to be changed for other users

    print("Starting...\n")

    gammas = [1.5,2,4,8]
    Qfn_experiment(gammas, output_dirr)
    print("\n...Done")