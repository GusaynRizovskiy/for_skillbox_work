class Unit():
    def __init__(self,name):
        self.__name = name
        self.__health = 100
    def get_uron(self,value):
        self.__health-=value
        print("Юнит получил урон {}, его уровень здоровья {}".format(value,self.__health))
    def get_name(self)->str:
        return self.__name
    def get_health(self) -> int:
        return self.__health
class Soldier(Unit):
    def __init__(self,name):
        super().__init__(name)
        self.__health = self.get_health()
    def get_uron(self,value):
        self.__health-=value
        print("Солдат получил урон {}, его уровень здоровья {}".format(value, self.__health))

class People(Unit):
    def __init__(self,name):
        super().__init__(name)
        self.__health = self.get_health()
    def get_uron(self,value):
        value = value*2
        self.__health-=value
        print("Гражданин получил урон {}, его уровень здоровья {}".format(value, self.__health))
p1 = People("Rudic")
p1.get_uron(45)
p1.get_uron(23)
p1.get_uron(17)
p2 = Soldier("Bumer")
p2.get_uron(45)
p2.get_uron(23)
p2.get_uron(17)

