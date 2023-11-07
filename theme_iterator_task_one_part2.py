def generator(N):
    for i in range(N+1):
        yield i**2
g = generator(9)
for i in g:
    print(i)