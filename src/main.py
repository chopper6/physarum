import networkx as nx, random as rd, numpy as np
import init, update


def run():
    num_iters = 80
    net, Adj ,L, R, D, Q, B, P = init.net_and_matrices(num_nodes=16, pr_edge = .5, init_type='random')

    #print("\nAT START: \n")
    #output(P,D,R,L)

    for i in range(num_iters):
        R, P, Q, D = update.update_net(net,Adj,L, R, D, Q, B, P)
        #if i % 10 == 0: print("potentials at iter " + str(i) + ' = ' + str(P))

    #print("\nAT END: \n")
    #output(P,D,R,L)

    compare_shortest_path(net, D, L, B)




def compare_shortest_path(net, D, L, B):

    for i in range(len(B)):
        if B[i] == 1: source = i
        elif B[i] == -1: target =i
    assert(source is not None and target is not None)

    weighted_net = nx.from_numpy_matrix(np.array(L))
    nx_path = nx.shortest_path(weighted_net, source, target)
    print("Networkx calculates shortest path as: " + str(nx_path))

    phys_path = []
    D_incld = []
    for i in range(len(D)):
        for j in range(len(D)):
            if D[i][j] > .1:
                phys_path.append(i) #i.e cut off edges to some threshold
                phys_path.append(j)

    phys_path = np.unique(phys_path)
    print("Physarum simulation calculates shortest path as: " + str(phys_path))
    print("Note path may be out of order.")

def output(P,D,R,L):
    print("\nPotentials: " + str(P))
    print("\nLengths: " + str(L))
    print("\nResistances: " + str(R))
    print("\nDiameter: " + str(D))


if __name__ == "__main__":
    print("Starting...\n")
    run()
    print("\n...Done")