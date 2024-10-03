from Graph import *
from Queue import *


NON_VISITE = 0
VISITE = 1
EN_VISITE = 2


def apply_bfs(g,s,f=None):
    '''
    input :
        - g : Graph
        - s : int index of the root node
        - f : function that takes a node and its parent in the
               BFS tree and performs whatever
    '''
    visited = [False]*len(g.nodes)
    tree = [-1]*len(g.nodes)
    distances = [-1]*len(g.nodes)
    q = Queue()
    q.enqueue(s)
    visited[s] = True
    tree[s] = s
    distances[s] = 0
    while not q.is_empty():
        node_i = q.dequeue()
        node = g.nodes[node_i]
        for edge in node.adj:
            if not visited[edge.head.index]:
                q.enqueue(edge.head.index)
                if f != None:
                    f(edge.head,node)
                visited[edge.head.index] = True
                tree[edge.head.index] = node_i
                distances[edge.head.index] = distances[node_i] + 1

    return (tree,distances)

def connected_component(g,s):
    '''
    input :
        - g : Graph
        - s : int index of a node
    output : 
        - [int] : list of indices of nodes connected to s
    '''
    cc = []
    apply_bfs(g,s,lambda x,_ : cc.append(x.index))
    return cc

def shortest_path(g,s,e):
    '''
    input :
        - g : Graph
        - s : int index of start node
        - e : int index of end node
    output : 
        - [int] : list of indices of nodes in path from s to e
    '''
    bfs_tree,distances = apply_bfs(g,s)
    if distances[e] == -1 :
        return [] # there is no path from s to e
    current = e
    path = [e]
    while current != s:
        current = bfs_tree[current]
        path.append(current)

    return path[::-1]

def visit_dfs(g,u,couleur,parent):
    if couleur[u] != NON_VISITE:
        return

    couleur[u] = EN_VISITE
    node_u = g.nodes[u]
    for edge in node_u.adj:
        node_v = edge.head
        if parent[node_v.index] == -1:
            parent[node_v.index] = u
        visit_dfs(g,node_v.index,couleur,parent)
    couleur[u] = VISITE

def DFS(g):
    couleur = [NON_VISITE]*len(g.nodes)
    parent = [-1]*len(g.nodes)
    for i,col in enumerate(couleur):
        if col == NON_VISITE:
            parent[i] = i
            visit_dfs(g,i,couleur,parent)
            parent[i] = -1

    return parent

def acyclique_rec(g,u,couleur):
    if couleur[u] == VISITE:
        return True
    if couleur[u] == EN_VISITE:
        print("Cycle found, ends at",u,g.nodes[u].name)
        return False

    couleur[u] = EN_VISITE
    node_u = g.nodes[u]
    for edge in node_u.adj:
        node_v = edge.head
        acyclique_rec(g,node_v.index,couleur)
    couleur[u] = VISITE
    return True

def acyclique(g):
    couleur = [NON_VISITE]*len(g.nodes)
    for i,col in enumerate(couleur):
        if col == NON_VISITE:
            if not acyclique_rec(g,i,couleur):
                return False
    return True

def make_acyclique_rec(g,u,couleur):
    if couleur[u] == VISITE:
        return
    assert(couleur[u] != EN_VISITE)

    couleur[u] = EN_VISITE
    node_u = g.nodes[u]
    to_remove = []
    for edge in node_u.adj:
        node_v = edge.head
        v = node_v.index
        if couleur[v] == EN_VISITE:
            to_remove.append(v)
        elif couleur[v] == NON_VISITE:
            make_acyclique_rec(g,v,couleur)

    for v in to_remove:
        g.remove_edge(u,v)
    couleur[u] = VISITE

def make_acyclique(g):
    couleur = [NON_VISITE]*len(g.nodes)
    for i,col in enumerate(couleur):
        if col == NON_VISITE:
            make_acyclique_rec(g,i,couleur)

def topo_sort_rec(g,u,couleur,order):
    if couleur[u] == VISITE:
        return
    assert(couleur[u] != EN_VISITE)

    couleur[u] = EN_VISITE
    node_u = g.nodes[u]
    for edge in node_u.adj:
        node_v = edge.head
        v = node_v.index
        if couleur[v] == NON_VISITE:
            topo_sort_rec(g,v,couleur,order)
    order.append(u)

def topo_sort(g):
    couleur = [NON_VISITE]*len(g.nodes)
    order = []
    for i,col in enumerate(couleur):
        if col == NON_VISITE:
            topo_sort_rec(g,i,couleur,order)

    return order[::-1]

if __name__=="__main__":
    g = Graph([c for c in "abcdefgh"])
    A=[[0,1],[0,6],[1,0],[1,2],[1,4],[2,0],[2,5],[4,2],[4,6],[5,3],[6,1],[6,7],[7,2],[7,3],[7,5]]
    for [i,j] in A:
        g.add_edge(i,j)

    print("========ADJ_LIST==========")
    g.print_adj_list()

    print("===========BFS============")
    apply_bfs(g,0,lambda x,_: print(x.name))
    print("===========CC=============")
    print(f"connected_component of {g.nodes[0].name} is ", [g.nodes[i].name for i in connected_component(g,0)])
    print("=======Distance===========")
    bfs_tree,distances = apply_bfs(g,0)
    for i,d in enumerate(distances):
        print(f"distance from {g.nodes[0].name} to {g.nodes[i].name} is {d}")
    print("=====Shortest Path========")
    for i,j in [(0,2),(2,0),(4,5),(6,6)]:
        print(f"Shortest path from {g.nodes[i].name} to {g.nodes[j].name} is {[g.nodes[k].name for k in shortest_path(g,i,j)]}")
    print("===========DFS============")
    print(DFS(g))
    print("=========Acyclic==========")
    print(f"g is {'not' if not acyclique(g) else ''} acyclic")
    print("=======Make Acyclic=======")
    print("make_acyclique(g)")
    make_acyclique(g)
    g.print_adj_list()
    print(f"g is {'not' if not acyclique(g) else ''} acyclic")
    print("=========Topo Sort========")
    print([g.nodes[i].name for i in topo_sort(g)])
