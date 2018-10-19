import numpy as np
from scipy import linalg
'''
R - resistance
Q - current
P - potential
D - diameter
L - length
R, D, Q, B, P
'''

def update_net(net,Adj,L, R, D, Q, B, P):
    R = updateR(L,D,R)
    P = updateP(Adj, B,P,R,net)
    Q = updateQ(Adj,Q,P,R)
    D = updateD(Q,D)
    return R,P,Q,D


def updateR(L,D,R):
    s = (len(L[0]))
    for i in range(s):
        for j in range(s):
            if D[i][j] != 0:
                R[i][j] = max(L[i][j]/D[i][j],.0000001)
    return R

def updateP(Adj, B,P,R,net):
    s = len(P)
    X = [[0 for i in range(s)] for j in range(s)]

    for i in range(s):
        for j in range(s):
            if Adj[i,j] == 1:
                    #and B[i] != -1: #ie are nghs and output potential is set to 0
                X[i][j] = 1/R[i][j]   # poss rev +- in next two lines
                if B[i] != -1: X[i][i] -= 1/R[i][j]


    #print("\n about to solve P, X looks like: \n" + str(X) + "\n\n")
    #soln = linalg.solve(X,B)
    #P=soln

    soln = linalg.lstsq(X,B)
    P = soln[0]
    #print('\nsoln to p = ' + str(P))
    return P

def updateQ(Adj,Q,P,R):
    s = len(P)
    Q = [[0 for i in range(s)] for j in range(s)]
    for i in range(s):
        for j in range(s):
            if Adj[i,j]==1:
                Q[i][j] = (P[i]-P[j])/R[i][j]
    return Q

def updateD(Q,D):
    #TODO can change hidden constant k, affects convergence speed
    D = np.divide(np.add(np.abs(Q), D),2)
    return D



