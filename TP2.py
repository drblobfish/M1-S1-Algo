import numpy as np
import time
import matplotlib.pyplot as plt

def longueur_plsc_rec(S,R,i,j):
    if i<0 or j<0:
        return 0
    if S[i]==R[j] :
        return longueur_plsc_rec(S,R,i-1,j-1) + 1
    return max(longueur_plsc_rec(S,R,i-1,j),
            longueur_plsc_rec(S,R,i,j-1))



def longueur_plsc(S,R):
    # breakpoint()
    L = np.zeros((len(S)+1,len(R)+1),dtype=int)
    C = np.zeros((len(S),len(R)),dtype=np.uint8)
    for i in range(len(S)):
        for j in range(len(R)):
            if S[i]==R[j]:
                L[i+1,j+1] = L[i,j] + 1
                C[i,j] = 0
            elif L[i+1,j] > L[i,j+1]:
                L[i+1,j+1] = L[i+1,j]
                C[i,j] = 1
            else :
                L[i+1,j+1] = L[i,j+1]
                C[i,j] = 2
    return (L[len(S),len(R)],L,C)

def plsc(S,R):
    (_,_,C) = longueur_plsc(S,R)
    i = len(S)-1
    j = len(R)-1
    sous_sequence = []
    while i>=0 and j>=0:
        if C[i,j] == 0:
            sous_sequence.append(S[i])
            i-=1
            j-=1
        elif C[i,j] == 1:
            j-=1
        else:
            i-=1
    return sous_sequence[::-1]


def perf_test(maxl,nbl,algo,log_scale=True):
    # breakpoint()
    if log_scale :
        lengths = np.geomspace(1,maxl,nbl).astype(int)
    else :
        lengths = np.linspace(1,maxl,nbl).astype(int)
    perf_time = np.zeros(nbl)
    for i,l in enumerate(lengths):
        seq1 = np.random.randint(0,9,l)
        seq2 = np.random.randint(0,9,l)

        t1 = time.perf_counter()
        algo(seq1,seq2)
        perf_time[i] = time.perf_counter() - t1

    plt.plot(lengths,perf_time)
    plt.show()

if __name__=="__main__":
    perf_test(15,10,lambda S,R : longueur_plsc_rec(S,R,len(S)-1,len(R)-1),log_scale=False)
    perf_test(2000,20,plsc)
