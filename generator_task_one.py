from collections.abc import Iterable
def generator()->Iterable:
    c = 0
    while True:
        yield c
        c+=1
ac = generator()
for i in ac:
    print(i)

