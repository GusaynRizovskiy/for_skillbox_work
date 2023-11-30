from typing import List
class Human:
    def __init__(self,age:int,name:str,gender:str)->None:
        self.__age = age
        self.__name = name
        self.__gender = gender
    def __str__(self):
        print("Я {gender}, меня зовут{name} и мне{age}.".format(gender=self.__gender,
                                                                name = self.__name,
                                                                age = self.__age))
    @property
    def age(self)->int:
        return self.__age
    @property
    def name(self)->str:
        return self.__name
    @property
    def gender(self)->str:
        return self.__gender
    @age.setter
    def age(self,value:int)->None:
        self.__age = value
    @name.setter
    def name(self,value:str)->None:
        self.__name = value
    @gender.setter
    def gender(self,value:str)->None:
        self.gender = value

    def __repr__(self):
        return f"({self.name}, {self.age})"
human_one = Human(23,"Jack","man")
human_two = Human(18,"Lily","woman")
human_three = Human(56,"Jon","man")
humans: List[Human] = [human_one,human_two,human_three]
sort_humans = sorted(humans,key=lambda elem:elem.age)
sort_humans_2 = sorted(humans,key=lambda elem:-elem.age)
print(sort_humans)
print(sort_humans_2)