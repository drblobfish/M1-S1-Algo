import numpy as np

class Task():
    def __init__(self,debut,fin,debut_inf = False, fin_inf = False):
        self.debut = debut
        self.debut_inf = debut_inf
        self.fin = fin
        self.fin_inf = fin_inf

    def __repr__(self):
        return f"Task(d={self.debut},f={self.fin})"

def creer_liste_activite(n,tmax,dmax):
    tlist = np.random.randint(0,tmax,n)
    dlist = np.random.randint(1,dmax,n)
    return [Task(t,t+d) for (t,d) in zip(tlist,dlist)]

def choix_activite_rec(A,i,j):
    Aij = list(filter(lambda k : (i.fin <= k.debut or i.fin_inf) and (k.fin <= j.debut or j.debut_inf), A))
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

def perf_test(maxl,nbl,algo,log_scale=True):
    # breakpoint()
    if log_scale :
        lengths = np.geomspace(1,maxl,nbl).astype(int)
    else :
        lengths = np.linspace(1,maxl,nbl).astype(int)
    perf_time = np.zeros(nbl)
    for i,l in enumerate(lengths):
        tasks = creer_liste_activite(l,l,int(l/3)+2)

        t1 = time.perf_counter()
        algo(tasks)
        perf_time[i] = time.perf_counter() - t1

    plt.plot(lengths,perf_time)
    plt.show()

if __name__=="__main__":
    tasks = creer_liste_activite(5,5,4)
    print(tasks)

    (best_size,best_set) = choix_activite_rec(tasks,Task(-1,0),Task(6,7))
    print(best_size)
    print(best_set)

    best_set2 = choix_activite_glouton(tasks)
    print(best_set2)

    perf_test(1000,20,choix_activite_glouton)
