from Graph import *
import random

class HeapPrim:
    """
    Un tas min.
    Chaque élément est un couple (sommet,clé)
    - où sommet est l'indice d'un sommet
    - où clé est entier, et où -1 signifie +inf
    L'ordre sur les élément est l'ordre sur les clés
    Le tableau self.pos assigne à chaque sommet sa position
    dans self.items et doit être gardé à jour à chaque swap
    """
    def __init__(self,g : Graph):
        self.max_size = len(g.nodes)
        self.size = 0
        self.items = [None]*self.max_size
        self.pos = [None]*self.max_size

        self.INF = -1
        for i,_ in enumerate(g.nodes):
            self.insert((i,self.INF))

    def empty(self):
        return self.size == 0

    def extend_size(self,step):
        self.max_size += step
        self.items.extend([None]*step)

    def is_lower(self,i,j):
        key_i = self.items[i][1]
        key_j = self.items[j][1]
        return key_j==self.INF or (key_i<key_j and key_i != self.INF)

    def node_exist(self,i):
        return 0 <= i < self.size

    def swap(self,i,j):
        # update the pos array
        vertex_i = self.items[i][0]
        vertex_j = self.items[j][0]
        self.pos[vertex_i] = j
        self.pos[vertex_j] = i

        # swap
        tmp = self.items[i]
        self.items[i] = self.items[j]
        self.items[j] = tmp

    def heapify(self,i):
        if not self.node_exist(2*i+1):
            # no children:
            return
        if not self.node_exist(2*i+2):
            # only left child exist
            if self.is_lower(2*i+1,i):
                self.swap(2*i+1,i)
                self.heapify(2*i+1)
            return

        # all children exist
        child1 = 2*i+1
        child2 = 2*i+2
        if self.is_lower(i,child1) and self.is_lower(i,child2):
            # the tree[i] is a min heap
            pass
        else :
            # we need to swap i with one of its children
            if self.is_lower(child1,child2):
                self.swap(child1,i)
                self.heapify(child1)
            else :
                self.swap(child2,i)
                self.heapify(child2)

    def heapify_iter(self,i):
        flag_continue = True
        while flag_continue:
            if not self.node_exist(2*i+1):
                # no children => stop
                flag_continue = False
            elif not self.node_exist(2*i+2):
                # a single child
                if self.is_lower(i,2*i+1):
                    flag_continue = False
                else :
                    self.swap(2*i+1,i)
                    i = 2*i+1
            else :
                # all children exist
                child1 = 2*i+1
                child2 = 2*i+2
                if self.is_lower(i,child1) and self.is_lower(i,child2):
                    flag_continue = False
                else :
                    # we need to swap i with one of its children
                    if self.is_lower(child1,child2):
                        self.swap(child1,i)
                        i = child1
                    else :
                        self.swap(child2,i)
                        i = child2

    def percolate(self,i):
        flag_continue = True
        while flag_continue:
            parent = (i-1)//2
            if i == 0:
                flag_continue = False
            elif self.is_lower(i,parent):
                self.swap(parent,i)
                i = parent
            else :
                flag_continue = False

    def extract(self,i):
        assert self.node_exist(i) , "Tried to extract inexistant node"
        extracted_value = self.items[i]
        self.pos[extracted_value[0]] = None
        
        if self.is_lower(i,self.size-1):
            #swap for last value
            last_item = self.items[self.size-1]
            self.items[i] = last_item
            self.items[self.size-1] = None
            self.size -= 1

            # update pos array
            self.pos[last_item[0]] = i

            self.heapify(i)
        else :
            #swap for last value
            last_item = self.items[self.size-1]
            self.items[i] = last_item
            self.items[self.size-1] = None
            self.size -= 1

            # update pos array
            self.pos[last_item[0]] = i

            self.percolate(i)

        return extracted_value

    def insert(self,value):
        if self.size >= self.max_size:
            self.extend_size(self.size)
        
        self.size += 1
        self.items[self.size-1] = value
        self.pos[value[0]] = self.size-1
        self.percolate(self.size-1)

    def is_in(self,vertex):
        return self.pos[vertex] != None

    def decrease_key(self,vertex,new_value):
        self.items[self.pos[vertex]] = (vertex,new_value)
        self.percolate(self.pos[vertex])


def prim(g : Graph,s):
    n = len(g.nodes)
    hp = HeapPrim(g)
    parent = [None]*n

    hp.decrease_key(s,0)

    while not hp.empty():
        (vertex,key) = hp.extract(0)
        # print("extracted vertex",vertex)

        current_frame = g.nodes[vertex].adj.head
        while current_frame != None :
            edge = current_frame.data
            neighbour_vertex = edge.head.index
            if hp.is_in(neighbour_vertex):
                (_,neighbour_key) = hp.items[hp.pos[neighbour_vertex]]
                # print("neighbour vertex",neighbour_vertex,"key",neighbour_key,"edge weight",edge.w)
                if neighbour_key == -1 or neighbour_key > edge.w:
                    # print("decrease")
                    hp.decrease_key(neighbour_vertex,edge.w)
                    parent[neighbour_vertex] = vertex

            current_frame = current_frame.next

    return parent

def dijkstra(g:Graph,s):
    n = len(g.nodes)
    hp = HeapPrim(g)
    parent = [None]*n

    hp.decrease_key(s,0)

    while not hp.empty():
        (vertex,key) = hp.extract(0)
        # print("extracted vertex",vertex)

        current_frame = g.nodes[vertex].adj.head
        while current_frame != None :
            edge = current_frame.data
            neighbour_vertex = edge.head.index
            if hp.is_in(neighbour_vertex):
                (_,neighbour_key) = hp.items[hp.pos[neighbour_vertex]]
                # print("neighbour vertex",neighbour_vertex,"key",neighbour_key,"edge weight",edge.w)
                if neighbour_key == -1 or neighbour_key > key + edge.w:
                    # print("decrease")
                    hp.decrease_key(neighbour_vertex,key + edge.w)
                    parent[neighbour_vertex] = vertex

            current_frame = current_frame.next

    return parent

if __name__=="__main__":
    l=['a','b','c','d','e']
    g=Graph(l)
    for i in range(len(l)):
        for j in range(len(l)):
            if i!=j:
                weight = random.randint(-10,10)
                if weight > 0:
                    g.add_edge(i,j,weight)
    g.print_adj_list()
    print()

    print("PRIM")
    print(prim(g,0))
    print()

    print("DIJKSTRA")
    print(dijkstra(g,0))
