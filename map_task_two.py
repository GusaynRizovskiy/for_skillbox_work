import string
stroka = str(input("Введите строку: "))
print(list(filter(lambda elem: not (elem.isupper() or elem.isdigit()),stroka)))