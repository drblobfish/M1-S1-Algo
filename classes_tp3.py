# -*- coding: utf-8 -*-

class Stack:
    '''
        class for stack, use a Python list
        attributes :
        - size : int 
        - items : list
        methods :
        - push(x) : push the data x which is an instance of Item 
        - pop() : if the stack is not empty, pop and return the data, else do nothing and return None
        - print() : print the attributes
    '''
    def __init__(self):  # fonction d'initialisation d'une nouvelle instance (objet) de la classe
        self.size = 0
        self.items = list()
    
    def push(self,x):
        self.size += 1
        self.items.append(x)

    def pop(self):
        if self.size>0:
            self.size -= 1
            return self.items.pop()
        return None
        
    def print(self):  # fonction d'affichage de la pile
        print('size=',self.size,', items=',self.items)

class Queue:
    '''
        class for queue, use a Python list
        attributes :
        - items : list
        methods :
        - empty() : True if queue is empty
        - queue()
        - dequeue() : throws an error if queue is empty
    '''
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items)==0

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def __repr__(self):
        return self.items.__repr__()


class Node: 
    '''
        Class for nodes of a binary tree
        Attributes :
        - left : None or Node
        - right : None or Node
        - data : Item
    '''
    def __init__(self,v):
        self.left = None
        self.right = None
        self.data = v

    def __repr__(self):
        return f"Node(data = {self.data})"


class Tree:
    '''
        Class for binary tree
        Attributes :
        - size : int
        - root : None or Node
        Methods :
        - infix_print() : print the tree according infix order
    '''
    def __init__(self):
        self.root = None
        self.size = 0
 
    def infix_print_rec(self,root):
        if root is not None:
            self.infix_print_rec(root.left)
            print(root.data, end=', ')
            self.infix_print_rec(root.right)

    def infix_print(self):
        print("Tree : ", end='')
        self.infix_print_rec(self.root)
        print()

    def breadth_first_print(self):
        q = Queue()
        q.enqueue(self.root)
        while not q.empty():
            n = q.dequeue()
            if n != None:
                print(n.data)
                q.enqueue(n.left)
                q.enqueue(n.right)

    def depth_first_print(self):
        s = Stack()
        s.push(self.root)
        while not s.size == 0:
            n = s.pop()
            if n != None:
                print(n.data)
                s.push(n.left)
                s.push(n.right)

                
class BST(Tree):
    '''
        Class for ABR
        Derivate from Tree
    '''

    def search(self,item):
        return self.search_rec(self.root,item)

    def search_parent(self,item):
        if self.root == None:
            return None
        return self.search_parent_rec(item,self.root)

    def search_rec(self,root,item):
        if root == None:
            return None
        if root.data == item:
            return root
        if root.data < item:
            return self.search_rec(root.right,item)
        return self.search_rec(root.left,item)

    def search_parent_rec(self,item,root):
        # we assume root != None and root.data != item
        if item > root.data :
            if root.right == None:
                return root
            if root.right.data == item:
                return root
            return self.search_parent_rec(item,root.right)
        if root.left == None:
            return root
        if root.left.data == item:
            return root
        return self.search_parent_rec(item,root.left)
        

    def min(self):
        if self.root == None :
            return None
        return self.min_rec(self.root)

    def min_rec(self,root):
        if root.left == None:
            return root.data
        return self.min_rec(root.left)

    def insert(self,item):
        if self.root == None:
            self.root = Node(item)
        else :
            self.insert_rec(Node(item),self.root)

    def insert_rec(self,node,root):
        # we assume root is not None
        if node == None:
            return
        if root.data == node.data:
            return
        if root.data > node.data:
            if root.left == None:
                root.left = node
                return
            self.insert_rec(node,root.left)
            return
        if root.right == None:
            root.right = node
            return
        self.insert_rec(node,root.right)

    def suppress(self,item):
        if self.root == None:
            return None
        if self.root.data == item:
            node = self.root
            self.root = node.right
            self.insert_rec(node.left,self.root)
            node.right = None
            node.left = None
            return node
        # we know root is not the node to be suppressed
        parent = self.search_parent_rec(item,self.root)
        if parent == None:
            return None
        if parent.data > item:
            if parent.left == None:
                return None
            node = parent.left
            parent.left = node.left
            self.insert_rec(node.right,parent)
            node.left = None
            node.right = None
            return node
        # so parent.data < item
        if parent.right == None:
            return None
        node = parent.right
        parent.right = node.left
        self.insert_rec(node.right,parent)
        node.left = None
        node.right = None
        return node

    def successor(self,x):
        return self.successor_rec(self.root,x,None)

    def successor_rec(self,root,x,best_succ):
        if root == None:
            return best_succ
        if root.data == x :
            return self.successor_rec(root.right,x,best_succ)
        if root.data > x:
            if best_succ == None:
                return self.successor_rec(root.left,x,root.data)
            elif root.data < best_succ:
                return self.successor_rec(root.left,x,root.data)
            else :
                return self.successor_rec(root.left,x,best_succ)
        if root.data < x:
            return self.successor_rec(root.right,x,best_succ)

        

class ArrayStack:
    '''
        attributes :
        - size : int 
        - items : list
        methods :
        - push(x) : push the data x which is an instance of Item 
        - pop() : if the stack is not empty, pop and return the data, else do nothing and return None
        - print() : print the attributes
    '''
    def __init__(self):
        self.size = 0
        self.capacity = 2**8
        self.list = [None]*self.capacity

    def push(self,x):
        if self.size >= self.capacity:
            self.allocate_longer()
        self.list[self.size] = x
        self.size +=1

    def allocate_longer(self):
        self.list = self.list + [None]*self.capacity
        self.capacity *= 2

    def pop(self):
        self.size -= 1
        return self.list[self.size]

    def __repr__(self):
        return self.list[:self.size].__repr__()

    def print(self):
        print(self)


class ArrayQueue:
    '''
        class for queue
        attributes :
        - items : list
        methods :
        - empty() : True if queue is empty
        - queue()
        - dequeue() : throws an error if queue is empty
    '''

    def __init__(self):
        self.start = 0
        self.size = 0
        self.capacity = 2**8
        self.list = [None]*self.capacity

    def empty(self):
        return self.size <= 0

    def queue(self,x):
        if self.size >= self.capacity:
            self.allocate_longer()
        self.list[(self.start+self.size) % self.capacity] = x
        self.size += 1

    def allocate_longer(self):
        new_list = [None] * (2*self.capacity)
        for i in range(self.size):
            new_list[i] = self.list[(self.start+i) % self.capacity]
        self.capacity *= 2
        self.list = new_list

    def dequeue(self):
        elem = self.list[self.start]
        self.size -= 1
        self.start = (self.start + 1) % self.capacity
        return elem

    def __repr__(self):
        return "[" + ", ".join(str(self.list[(self.start+i) % self.capacity]) for i in range(self.size)) + "]"


class LLNode:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

class LLStack:
    '''
        stack as a linked list
        attributes :
        - size : int 
        - top : LLNode
        methods :
        - push(x) : push the data x which is an instance of Item 
        - pop() : if the stack is not empty, pop and return the data, else do nothing and return None
        - print() : print the attributes
    '''
    def __init__(self):
        self.size = 0
        self.top = None

    def push(self,x):
        self.size += 1
        node = LLNode(x)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.size <= 0:
            raise Exception("Empty Stack") 
        self.size -= 1
        node = self.top
        self.top = node.next
        return node.data

    def __repr__(self):
        return f"LLStack(size = {self.size}, top = {self.top})"

    def print(self):
        print(self)

class LLQueue:
    '''
    Queue as a linked list
    attributes :
        - size : int 
        - start : LLNode (links go from end to start)
        - end : LLNode
    methods :
        - empty() : True if queue is empty
        - queue()
        - dequeue() : throws an error if queue is empty
    '''

    def __init__(self):
        self.size = 0
        self.start = None
        self.end = None

    def empty(self):
        return self.size <= 0

    def queue(self,x):
        node = LLNode(x)
        if self.empty():
            self.start = node
            self.end = node
        else :
            self.start.next = node
            self.start = node
        self.size +=1

    def dequeue(self):
        if self.empty():
            raise Exception("Empty Queue")
        node = self.end
        self.end = node.next
        self.size -= 1
        if self.empty():
            self.start = None
        return node.data
    
    def __repr__(self):
        return f"LLQueue(size = {self.size}, start = {self.start}, end = {self.end})"

################################  Tests  ################################## 

s=Stack()
s.print()
s.push(1)
s.print()
s.push(2)
s.print()
s.pop()
s.print()
s.pop()
s.print() 

###### BST ########       

t = BST()
for i in [3,5,1,6,7,8,2,9]:
    t.insert(i)
t.infix_print()

for i in [0, 2, 3, 5, 15]:
    print(f"search({i}) = {t.search(i)}")

print(f"t.min() = {t.min()}")

t.suppress(3)
print("t.suppress(3)")
t.infix_print()

t.suppress(1)
print("t.suppress(1)")
t.infix_print()
print(f"t.min() = {t.min()}")

for i in [0, 2, 3, 5, 8, 9, 15]:
    print(f"t.successor({i}) = {t.successor(i)}")

#t.depth_first_print()
#t.breadth_first_print()


###### ArrayStack ########       

s = ArrayStack()
for i in range(300):
    s.push(i)
print(s)
for i in range(300):
    s.pop()
print(s)

    
###### ArrayQueue ########       

q = ArrayQueue()
for i in range(300):
    q.queue(i)
print(q)
for i in range(300):
    q.dequeue()
print(q)


###### LLStack  ########       

s = LLStack()
for i in range(300):
    s.push(i)
print(s)
for i in range(300):
    s.pop()
print(s)

###### LLQueue  ########       

q = LLQueue()
for i in range(300):
    q.queue(i)
print(q)
for i in range(300):
    q.dequeue()
print(q)
