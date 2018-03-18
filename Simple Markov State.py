import numpy as np
import quantecon as qe

def markov_state(P,a,n):
    P = np.asarray(P)
    X = np.empty(n,dtype=int)
    X[0]=a
    l = len(P)
    P_dist = [qe.DiscreteRV(P[i,:]) for  i in range(l)]
    for i in range(n-1):
        X[i+1] = P_dist[X[i]].draw()
    return X

P = [[0.4,0.6],[0.2,0.8]]
a = 1
n = 10000
A = markov_state(P,a,n)
print (A)