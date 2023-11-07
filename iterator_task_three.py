import random


class New_iterator():
    def __init__(self,count:int)->None:
        self.last = 0
        self.start = 0
        self.end = count
    def __iter__(self):
        return self
    def __next__(self):
        self.start+=1
        if self.start>self.end:
            raise StopIteration
        else:
            self.last+=random.random()
            return self.last
id = New_iterator(7)
for el in id:
    print(el)