from collections import deque
iska = deque()
iska.append("Doc")
iska.append("Tom")
iska.append("Mark")
iska.appendleft("Rida_Solomon")
print(iska)
item = iska.popleft()
print(item)
list_one = [1,2,2,2,2,1,1,1,1,1,1,1,3,3,5,3,3,5,6,7,6]
from collections import Counter
print(Counter(list_one))
from collections import namedtuple
Point = namedtuple("Point",["x","y"])
p = Point(23,54)
print(p)