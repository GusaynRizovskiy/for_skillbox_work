class iterator():
    def __init__(self,N):
        self.N = N
        self.start = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.start>=self.N:
            raise StopIteration
        else:
            self.start+=1
            return self.start**2
id = iterator(10)
for element in id:
    print(element)
