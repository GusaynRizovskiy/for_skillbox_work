class Node:
    def __init__(self,value,next = None):
        self.value = value
        self.next = next
t1 = Node("Babito")
t2 = Node("Dona",t1)
