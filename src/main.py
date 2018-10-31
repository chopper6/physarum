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

    if accuracy != 0: convergence_iterations /= accuracy #accuracy is just #times converged right now
    accuracy /= num_reps
    if verbose:
        print("Accuracy = " + str(accuracy))
        print("Mean convergence iterations = " + str(convergence_iterations))
    #plot.accuracy(output_dirr)

    return accuracy, convergence_iterations


def Qfn_experiment(gammas, output_dirr, verbose=False):

    set_titles = ['Medium Dense', 'Large Sparse', 'Large Dense']
    #num_iters, num_reps = 200,20
    num_nodes, pr_edge = [80,200,200], [.8,.2,.8]
    assert(len(set_titles) == len(num_nodes))

    #num_nodes, pr_edge = [8, 8, 20, 20], [.2, .8, .2, .8]

    for i in range(len(set_titles)):
        print("\nStarting set " + str(set_titles[i]))
        num_iters = int(num_nodes[i]*pr_edge[i])
        num_reps = int(num_iters)

        gamma_acc = [None for i in range(len(gammas))]
        gamma_convg = [None for i in range(len(gammas))]

        for g in range(len(gammas)):
            if verbose: print("\n\n##########################################   GAMMA = "  +str(gammas[g]) + "   ##########################################\n")
            else:print("Testing gamma = " + str(gammas[g]))
            gamma_acc[g], gamma_convg[g] = run(num_iters, num_reps, output_dirr, Qfunction='alt', gamma=gammas[g], num_nodes=num_nodes[i], pr_edge=pr_edge[i])

        if verbose: print("\n\n##########################################   CONTROL   ##########################################\n")
        else:
            print("Testing control")
        control_acc, control_convg = run(num_iters, num_reps, output_dirr, num_nodes=num_nodes[i], pr_edge=pr_edge[i])
        plot.gamma_run(output_dirr, set_titles[i], gammas, gamma_acc, gamma_convg, control_acc, control_convg)


if __name__ == "__main__":

    #TODO: figs for results, does not account for mult poss shortest paths

    output_dirr = "C:/Users/Crbn/Documents/Code/physarum/test"
    #This is my local path and needs to be changed for other users

    print("Starting...\n")

    gammas = [1, 1.2, 1.4, 1.6, 1.8, 2, 3]
    Qfn_experiment(gammas, output_dirr)
    print("\n...Done")