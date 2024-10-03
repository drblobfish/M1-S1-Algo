# -*- coding: utf-8 -*-

################################  Graphs  ################################## 
import List
import Queue


class Adj_list(List.Linked_list): 
    '''
    class for a adjacency list
    
    attributes inherited from Linked_list :
    - head : Frame1 or None
    
    methods inherited from Linked_list :
    - is_empty() : return true is the queue is empty, false otherwise
    - append(x) : add the data x at the head 
    - pop() : if the linked list is not empty, pop the head, else do nothing and return None
    
    new method
    - print() : print the list of node name
    
    Dependencies : class Linked_list
'''

    def print(self):  # surcharge la methode print des listes pour afficher les noms des noeuds
        print("Liste d'adjacence = ",end='')
        current=self.head
        while current:
            edge=current.data
            print(edge.head.name,',',edge.w, end=' ; ')
            current=current.next
        print()    


class Node: 
    '''
    Class for nodes of a graph
    
    Attributes :
    - index : index of the node in the graph list
    - name : string (default '')
    - adj : Adj_list of Edge

    Dependencies : class Adj_list
    '''
    def __init__(self,index=0,name=''):
        self.index = index
        self.name = name
        self.adj = Adj_list()


class Edge: 
    '''
        Class for edges of a graph
        
        Attributes :
        - head : Node   # dans l'arc (x,y), y est nommé head en anglais (tete de la fleche), et x tail (queue de la fleche)
        - w : weight
    
    Dependencies : None
    '''
    def __init__(self,n,w=1):
        self.head = n  
        self.w = w


class Graph:
    '''
    Class for graph
    
    Attributes :
    - nodes : list (instance of list class) of Node  (default empty list)
    
    Methods :
    - add_edge(i,j,w=1) : if i and j are not out of range, add an edge between i and j with the weight w (default edge = 1), do nothing otherwise
    
    Dependencies : classes Node, Edge and Adj_list
    '''
    def __init__(self,l=[]):  # l est optionnel : liste ne noms de noeuds
        self.nodes=list()
        for i in range(len(l)):
            n=Node(i,l[i])
            self.nodes.append(n)
 
    def add_edge(self,i,j,w=1):
        if i<len(self.nodes) and j<len(self.nodes):
            e=Edge(self.nodes[j],w)
            self.nodes[i].adj.append(e)

    def remove_edge(self,i,j):
        if i<len(self.nodes) and j<len(self.nodes):
            self.nodes[i].adj.filter(lambda x : x.head.index != j)

            
    def print_adj_list(self):
        for n in self.nodes:
            print('Noeud :', n.index,n.name )
            n.adj.print()
    
                
################################  Tests  ################################## 
if __name__=="__main__":
    q=Queue.Queue()
    g1=Graph()
    print('Un graphe vide :')
    g1.print_adj_list()

    l=['a','b','c','e','f','d','g','h']
    g2=Graph(l)
    g2.add_edge(0,2)
    print()
    print('Un graphe avec un arc (0,2)')
    g2.print_adj_list()

    print("g2.remove_edge(0,2)")
    g2.remove_edge(0,2)
    g2.print_adj_list()
