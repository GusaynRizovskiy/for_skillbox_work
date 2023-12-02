import re
from typing import List
floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]
floats2: List[float] = [round(elem**3,3) for elem in floats]
names2: List[str] = [elem for elem in names if len(elem)>5]
result = 1
numbers2: List[int] = lambda x,y: 
print(floats2)
print(names2)
print(numbers2)