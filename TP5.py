

class Heap:
    def __init__(self,max_size=100):
        self.max_size = max_size
        self.size = 0
        self.items = [None]*self.max_size

    def extend_size(self,step):
        self.max_size += step
        self.items.extend([None]*step)

    def is_lower(self,i,j):
        return self.items[i]<self.items[j]

    def node_exist(self,i):
        return 0 <= i < self.max_size

    def swap(self,i,j):
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
            if self.is_lower(i,parent):
                self.swap(parent,i)
                i = parent
            else :
                flag_continue = False

    def extract(self,i):
        assert self.node_exist(i) , "Tried to extract inexistant node"
        extracted_value = self.items[i]
        
        if self.is_lower(i,self.size-1) # TBD

        #swap for last value
        self.items[i] = self.items[self.size-1]
        self.items[self.size-1] = None
        self.size -= 1

        if 
