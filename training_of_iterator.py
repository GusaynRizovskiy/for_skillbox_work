class iterat():
    def __init__(self,N:int):
        self.N = N
        self.i = 0
    def __iter__(self):
        self.i = 0
        return self
    def __next__(self):
        if self.i >= self.N:
            raise StopIteration
        else:
            self.i+=1
            return self.i**2
ak = iterat(8)
for i in ak:
    print(i)
print("\n")
def generator(N):
    for i in range(N+1):
        print(i**2)
akk = generator(7)

N = 9
print([i**2 for i in range(N+1)])