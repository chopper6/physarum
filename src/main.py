import networkx as nx, random as rd, numpy as np
import init, update, stats, output, plot


def run(output_dirr):
    num_iters = 200
    net, Adj ,L, R, D, Q, B, P = init.net_and_matrices(num_nodes=80, pr_edge = .4, init_type='random')
    output.init_output(output_dirr)
    #print("\nAT START: \n")

    #output(P,D,R,L)

    for i in range(num_iters):
        R, P, Q, D = update.update_net(net,Adj,L, R, D, Q, B, P)
        phys_path, nx_path = stats.extract_shortest_path(net, D, L, B)

        if i%20 == 0: print("2 paths: " + str(nx_path) + ", " + str(phys_path))

        true_pos, false_pos, true_neg, false_neg = stats.score(phys_path, nx_path, net, output_dirr + "/accuracy.csv")
        output.write_acc(true_pos, false_pos, true_neg, false_neg, i, output_dirr)

    plot.accuracy(output_dirr)

if __name__ == "__main__":

    #TODO: generally poor convergence; output should be avg of many runs

    output_dirr = "C:/Users/Crbn/Documents/Code/physarum/test"
    #This is my local path and needs to be changed for other users
    print("Starting...\n")
    #np.warnings.filterwarnings('ignore')
    #print("\nWARNING: all numpy warnings are currently suppressed, look at main function of main.py to change this.\n")

    run(output_dirr)
    print("\n...Done")