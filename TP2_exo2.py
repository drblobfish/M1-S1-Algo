import numpy as np

class Task():
    def __init__(self,debut,fin):
        self.debut = debut
        self.fin = fin

    def __repr__(self):
        return f"Task(d={self.debut},f={self.fin})"

def creer_liste_activite(n,tmax,dmax):
    tlist = np.random.randint(0,tmax,n)
    dlist = np.random.randint(1,dmax,n)
    return [Task(t,t+d) for (t,d) in zip(tlist,dlist)]

def choix_activite_rec(A,i,j):
    Aij = list(filter(lambda k : i.fin <= k.debut and k.fin <= j.debut,A))
    if len(Aij) == 0:
        return (0,Aij)
    best_size = 0
    best_set = []
    for k in Aij:
        (lsize,lset) = choix_activite_rec(Aij,i,k)
        (rsize,rset) = choix_activite_rec(Aij,k,j)
        if lsize + rsize + 1 > best_size:
            best_size = lsize + rsize + 1
            best_set = lset + rset + [k]

    return (best_size,best_set)


def choix_activite_glouton(A):
    At = sorted(A,key = lambda a : a.fin)
    C = []
    maxf = At[0].debut
    for a in At:
        if a.debut >= maxf:
            C.append(a)
            maxf = a.fin

    return C

if __name__=="__main__":
    tasks = creer_liste_activite(5,5,4)
    print(tasks)

    (best_size,best_set) = choix_activite_rec(tasks,Task(-1,0),Task(6,7))
    print(best_size)
    print(best_set)

    best_set2 = choix_activite_glouton(tasks)
    print(best_set2)
