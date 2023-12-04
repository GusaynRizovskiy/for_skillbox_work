from typing import List
spisok_one: List[int] = [2,2,3,4,5,6,7,8,9,10]
spisok_two: List[int] = [2,3,4,5,6,7,8,8,10,2]
finally_spisok = list(map(lambda x,y:x+y,spisok_one,spisok_two))
print(finally_spisok)

spisok_three: List[str] = ["cat","dog","frog","wolf"]
print(list(map(lambda elem: elem.capitalize(),spisok_three)))

result_even = list(filter(lambda elem:elem%2==0, finally_spisok))
print(result_even)

result_even_two = list(map(lambda elem:elem**3,filter(lambda elem:elem%2==0,result_even)))
result_even_three = sum(result_even_two)
print(result_even_three)