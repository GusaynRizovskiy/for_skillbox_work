import re
stroka = "ow much wood would a woodchuck chuck if a woodchuck could chuck wood?"
if re.match(r"wo",stroka):
    print("Yes")
else:
    print("No")
task_two = re.search("wo",stroka)
print("Первое упоминание в тексте сочетания ro: ",task_two)
print("Что упоминалось: ", task_two.group())
print("Начальная позиция: ",task_two.start())
print("Конечная позиция: ",task_two.end())
print(list(re.findall(r"wo",stroka)))
print(re.sub("wo","Замена",stroka))