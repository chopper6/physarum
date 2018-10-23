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

def update_net(Adj,L, R, D, Q, B, P, Qfunction='default', gamma=2):
    R = updateR(L,D,R)
    P = updateP(Adj, B,P,R)
    Q = updateQ(Adj,Q,P,R)
    prevD = D
    D = updateD(Q,D, Qfunction=Qfunction, gamma=gamma)

    converged, epsilon = True, .000001
    for i in range(len(D)):
        for j in range(len(D[0])):
            if (D[i][j] > prevD[i][j] + epsilon) or (D[i][j] < prevD[i][j] - epsilon):
                converged = False
                break
        if converged == False: break

    return R,P,Q,D, converged


def updateR(L,D,R):
    s = (len(L[0]))
    for i in range(s):
        for j in range(s):
            if D[i][j] != 0:
                R[i][j] = max(L[i][j]/D[i][j],.0000001)
    return R

def updateP(Adj, B,P,R):
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

def updateD(Q,D, Qfunction='default', gamma=2):
    #TODO can change hidden constant k, affects convergence speed

    if Qfunction == 'default' or Qfunction == 'identity':
        Qfn = np.abs(Q)

    elif Qfunction == 'alt':
        Q_gam = np.power(np.abs(Q), gamma)
        Qfn = np.divide(Q_gam,1+Q_gam)

    else: assert(False)

    D = np.divide(np.add(Qfn, D), 2)

    return D



