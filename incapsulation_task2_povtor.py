class Human():
    count = 0
    def __init__(self,name,age) -> None:
        self.__name = " "
        self.__age = 0
        self.set_age(age)
        self.set_name(name)
        Human.count += 1
    def get_name(self)->str:
        return self.__name
    def get_age(self)->int:
        return self.__age
    def set_name(self,value):
        if isinstance(value,str) and value.isalpha():
            self.__name = value
        else:
            raise ValueError("Ошибка в передачи имени")
    def set_age(self,value):
        if isinstance(value,int) and 0<=value<=100:
            self.__age = value
        else:
            raise ValueError("Ошибка в передачи возраста")
h1 = Human("Jack",43)
h2 = Human("Clotilda",-3)

