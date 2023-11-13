from typing import Any, Optional
class Node():
    def __init__(self,value:Optional[Any] = None,next: Optional["Node"] = None) -> None:
        self.value = value
        self.next = next
    def __str__(self) -> str:
        return "Node[{values}]".format(values = str(self.value))
class LinkedList():
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.cur_length = 0
    def __str__(self) ->str:
        if self.head is not None:
            current =self.head
            values = [str(current.value)]
            while current.next is not None:
                current = current.next
                values.append(str(current.value))
            return "[{values}]".format(values = " ".join(values))
        return "LinkedList []"
    def append(self,elem: Any) -> None:
        cur_node = Node(elem)
        if self.head is None:
            self.head = cur_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = cur_node
        self.cur_length += 1
    def remove(self,index):
        cur_index = 0
        cur_node = self.head
        if self.cur_length ==0 or self.cur_length < index:
            return
        if cur_node is not None:
            if index == 0:
                self.head = cur_node.next
                self.cur_length -=1
                return
        while cur_node is not None:
            if cur_index == index:
                break
            prev = cur_node
            cur_node = cur_node.next
            cur_index += 1
        prev.next = cur_node.next
list_one = LinkedList()
list_one.append(10)
list_one.append(20)
list_one.append(30)
list_one.append(40)
print(list_one)
list_one.remove(2)
print(list_one)
