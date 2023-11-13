from typing import Any,Optional
class Node():
    def __init__(self,value: Optional[Any] = None, next: Optional["Node"] = None) -> None:
        self.value = value
        self.next = next
    def __str__(self) -> str:
        return "Node [{value}]".format(value = str(self.value))
class LinkedList():
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.length = 0
    def __str__(self) ->str:
        if self.head is not None:
            current =self.head
            values = [str(current.value)]
            while current.next is not None:
                current = current.next
                values.append(str(current.value))
            return "[{values}]".format(values = " ".join(values))
        return "LinkedList []"
    def append(self,elem = Any) -> None:
        new_Node = Node(elem)
        if self.head is None:
            self.head = new_Node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_Node
        self.length+=1
    def remove(self,index):
        cur_node = self.head
        cur_index = 0
        if self.length == 0 or self.length < index:
            raise IndexError
        if cur_node is not None:
            if index == 0:
                self.head = cur_node.next
                self.length -= 1
                return
        while cur_node is not None:
            if cur_index == index:
                break
            prev = cur_node
            cur_node =cur_node.next
            cur_index +=1
        prev.next = cur_node.next
        self.length -= 1

mylist = LinkedList()
mylist.append(10)
mylist.append(20)
mylist.append(30)
print(mylist)
mylist.remove(1)
print(mylist)