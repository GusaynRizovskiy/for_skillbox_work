import random

n = int(input())
arr = [random.randint(0,101) for _ in range(n)]
iterator = arr.__iter__()
while True:
    try:
        print(iterator.__next__())
    except StopIteration:
        print("Конец итерации")
        break