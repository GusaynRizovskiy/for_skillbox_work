from typing import List
# def string_to_int(elem:str)->int:
#     return int(elem[4:])
user: List[str] = ["user1","user3","user32","user52","user2","user34"]
sorka = sorted(user,key=lambda elem:elem[4:])
print(sorka)