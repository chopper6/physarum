import networkx as nx, random as rd
import update, build_nets
import numpy as np

def net_and_matrices(num_nodes=8, pr_edge = .5, init_type ='3'):

    net = build_nets.seed(init_type)

    # MATRIX VERSION
    Adj = nx.adjacency_matrix(net).todense()
    print('Starting Adj matrix = ' + str(Adj))
    s = np.shape(Adj)[0]

    # EDGE MATRICES
    if init_type == '3': L = [[0,2,0],[2,0,3],[0,3,0]]
    else: L = [[0 for i in range(s)] for j in range(s)]
    print(L)
    D = [[0 for i in range(s)] for j in range(s)]
    Q = [[0 for i in range(s)] for j in range(s)]
    R = [[0 for i in range(s)] for j in range(s)]
    for i in range(s):
        for j in range(i):
            if Adj[i,j] == 1:
                if init_type != '3':
                    L[i][j] = rd.random()
                    L[j][i] = L[i][j]
                D[i][j] = rd.random()
                D[j][i] = D[i][j]
    update.updateR(L,D,R)

    # NODE MATRICES
    B = [0 for i in range(s)]
    P = [0 for i in range(s)]

    # PICK INPUT & OUTPUT
    input_index = rd.randint(0,s-1)
    B[input_index] = 1

    output_index = input_index
    while (output_index == input_index):
        output_index = rd.randint(0,s-1)
    B[output_index] = -1

    return net, Adj, L, R, D, Q, B, P




def cut_out(net):
    for edge in net.edges():
        net[edge[0]][edge[1]]['L'] = rd.random() #should be fixed
        net[edge[0]][edge[1]]['D'] = rd.random() #changes dynamically

        net[edge[0]][edge[1]]['Q'] = 0

        net[edge[0]][edge[1]]['R'] = update.calc_R(net[edge[0]][edge[1]]['L'],net[edge[0]][edge[1]]['D'])

        assert(net[edge[0]][edge[1]]['R'] != 0)

    for node in net.nodes():
        net.node[node]['B'] = 0
        net.node[node]['P'] = 0
        net.node[node]['ID'] = 'hidden'

    input = rd.choice(net.nodes())
    net.node[input]['B'] = 1
    net.node[input]['ID'] = 'input'
    output = input
    while (output == input):  # ie make sure diff input and output nodes
        output = rd.choice(net.nodes())
    net.node[output]['B'] = -1
    net.node[output]['ID'] = 'output'
