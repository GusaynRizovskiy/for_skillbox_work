def  Primes(N):
    arr = []
    for i in range(2,N+1):
        count = 0
        for j in arr:
            if i%j==0:
                break
        else:
            arr.append(i)
            yield i
prime_nums = Primes(50)

for i_elem in prime_nums:
    print(i_elem, end=' ')