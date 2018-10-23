import networkx as nx, random as rd

def seed(init_type, num_nodes, pr_edge):
    if init_type == 'random':
        net = nx.gnp_random_graph(num_nodes, pr_edge)  # TODO: may not be connected, also make explicitly undirected?

    elif init_type == '3': net = toy_model()

    undir_net = net.to_undirected()
    ensure_single_cc(undir_net)
    assert(nx.number_connected_components(undir_net) == 1) #TODO: problem if interrupts many runs
    return undir_net

def toy_model():
    net = nx.empty_graph()
    net.add_nodes_from([0,1,2])
    net.add_edges_from([(0,1),(1,2)])
    return net




#may be hard to read since originally from a different model
def ensure_single_cc(net):
    # WARNING: if not single connected component will randomly ADD EDGES util single connected component

    net_undir = net.to_undirected()
    num_cc = nx.number_connected_components(net_undir)

    j=0
    while (num_cc != 1):
        components = list(nx.connected_components(net_undir))
        constraints_check = False

        i = 0
        while not constraints_check:
            c1 = components[0]
            node1 = rd.sample(c1, 1)
            node1 = node1[0]

            c2 = components[1]
            node2 = rd.sample(c2, 1)
            node2 = node2[0]

            if net.has_edge(node1, node2) or net.has_edge(node2, node1):
                i += 1
                if (i >= 100000):
                    assert(False) #shouldn't be looping so many time
            else: constraints_check = True #only exist loop if found a viable edge not already in net

        net.add_edge(node1, node2)

        net_undir = net.to_undirected()
        num_cc = nx.number_connected_components(net_undir)
        j+=1
        if (j >= 100000):
            assert (False)  # shouldn't be looping so many time

    return net