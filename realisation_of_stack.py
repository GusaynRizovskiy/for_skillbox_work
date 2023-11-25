class stack:
    def __init__(self) -> None:
        self.arr = []
    def push(self,value):
        self.arr.append(value)
    def pop(self)->None:
        self.arr.pop()
    def __str__(self):
        return str(self.arr)
class Text_manager:
    def __init__(self) -> None:
        self.dic = dict()
    def new_task(self,task,priority):
        if priority not in self.dic:
            self.dic[priority] = stack()
        self.dic[priority].push(task)

