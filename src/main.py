import networkx as nx, random as rd
import init, update


def run():
    num_iters = 40
    net, Adj ,L, R, D, Q, B, P = init.net_and_matrices(num_nodes=3, pr_edge = .5, init_type='3')

    print("\nAT START: \n")
    output(P,D,R,L)

    for i in range(num_iters):
        R, P, Q, D = update.update_net(net,Adj,L, R, D, Q, B, P)
        #if i % 10 == 0: print("potentials at iter " + str(i) + ' = ' + str(P))

    print("\nAT END: \n")
    output(P,D,R,L)



def output(P,D,R,L):
    print("\nPotentials: " + str(P))
    print("\nLengths: " + str(L))
    print("\nResistances: " + str(R))
    print("\nDiameter: " + str(D))


if __name__ == "__main__":
    print("Starting...\n")
    run()
    print("\n...Done")