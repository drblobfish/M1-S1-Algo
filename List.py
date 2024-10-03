# -*- coding: utf-8 -*-

################################  Linked_list  ################################## 

class Frame:
    '''
    attributes :
    - data :  
    - next : next Frame or None
    
    Dependencies : None
    '''
    def __init__(self,x):
        self.data=x
        self.next=None


class Linked_list_iterator:
    def __init__(self,frame):
        self.frame = frame
    def __next__(self):
        if self.frame == None:
            raise StopIteration
        val = self.frame.data
        self.frame = self.frame.next
        return val

        
class Linked_list:
    '''
    class for a linked list
    
    attributes :
    - head : Frame or None
    
    methods :
    - is_empty() : return true is the list is empty, false otherwise
    - append(x) : add the data x at the head 
    - pop() : if the linked list is not empty, pop the head, else do nothing and return None
    - print() : print the list
    
    Dependencies : class Frame
    '''
    def __init__(self):
        self.head=None

    def __iter__(self):
        return Linked_list_iterator(self.head)

    def is_empty(self):
        return self.head is None
        
    def append(self,x):
        new_head = Frame(x)
        new_head.next = self.head
        self.head = new_head

    def pop(self):
        if self.head is None:
            return None
        x=self.head.data
        self.head=self.head.next
        return x

    def filter_rec(self,cond,frame):
        if frame == None:
            return frame
        if cond(frame.data):
            frame.next = self.filter_rec(cond,frame.next)
            return frame
        else :
            return self.filter_rec(cond,frame.next)

    def filter(self,cond):
        '''
        cond : predicate on the data
        '''
        self.head = self.filter_rec(cond,self.head)

    def print(self):  # fonction d'affichage de la liste
        print('Liste chainees= ',end='')
        current=self.head
        while current:
            print(current.data,end=' ')
            current=current.next
        print()    
################################  Tests  ################################## 
if __name__=="__main__":
    print()       
    l=Linked_list()
    for i in range(20):
        l.append(i)
    l.print()

    l.filter(lambda x : x!=12)
    l.print()

    l.filter(lambda x : x%2 == 0)
    l.print()
