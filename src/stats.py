import numpy as np, networkx as nx

def score(phys_path, nx_path, net, out_file):
    # NOT USED

    # node based score
    correct = True #start correct, then change if hit ANY mistake (conservative error)

    total = len(net.nodes())
    true_pos, false_pos, true_neg, false_neg = 0,0,0,0
    for ele in nx_path:
        if ele in phys_path:
            true_pos += 1
        else:
            true_neg += 1
            correct = False

    for ele in phys_path:
        if ele not in nx_path:
            false_pos += 1
            correct = False

    false_neg = (total - true_pos - true_neg - false_pos)/total

    true_pos /= total
    false_pos /= total
    true_neg /= total

    return true_pos, false_pos, true_neg, false_neg, correct




def extract_shortest_path(D, L, B):
    verbose = False

    for i in range(len(B)):
        if B[i] == 1: source = i
        elif B[i] == -1: target =i
    assert(source is not None and target is not None)

    weighted_net = nx.from_numpy_matrix(np.array(L, dtype=[('weight', float)]))
    nx_path = nx.shortest_path(weighted_net, source, target, weight = 'weight')
    if verbose: print("Networkx calculates shortest path as: " + str(nx_path))

    phys_path, diams = [], []
    for i in range(len(D)):
        for j in range(i):
            if D[i][j] > .1:
                phys_path.append(i) #i.e cut off edges to some threshold
                phys_path.append(j)
                diams.append(D[i][j])

    phys_path = np.unique(phys_path)

    if verbose:
        print("Physarum simulation calculates shortest path as: " + str(phys_path))
        print("With edge Diameters = " + str(diams))
        print("Note path may be out of order.")

    return phys_path, nx_path