import networkx as nx

def seed(init_type):
    if init_type == 'random':
        net = nx.gnp_random_graph(num_nodes, pr_edge)  # TODO: may not be connected, also make explicitly undirected?
        # TODO: make undirected

    elif init_type == '3': net = toy_model()

    return net

def toy_model():
    net = nx.empty_graph()
    net.add_nodes_from([0,1,2])
    net.add_edges_from([(0,1),(1,2)])
    return net
