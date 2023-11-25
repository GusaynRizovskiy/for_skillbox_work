from abc import ABC,abstractmethod
from math import pi,sqrt
class Shape(ABC):
    @staticmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,r):
        self.__r = r
    def area(self) -> float:
        return self.__r**2*pi
    def __str__(self):
        return "Площадь круга: {}".format(self.area())
class Rectangle(Shape):
    def __init__(self,a,b)->None:
        self.__a = a
        self.__b = b
    def area(self) -> float:
        return self.__a*self.__b
    def __str__(self):
        return "Площадь прямоугольника: {}".format(self.area())
class Trinagle(Shape):
    def __init__(self,a,b,c) -> None:
        self.__a = a
        self.__b = b
        self.__c = c
    def area(self) -> float:
        p = (self.__a + self.__b + self.__c)/2
        s = sqrt(p*(p-self.__a)*(p-self.__b)*(p-self.__c))
        return s
    def __str__(self):
        return "Площадь треуголника: {}".format(self.area())
t1 = Trinagle(3,4,5)
t2 = Circle(6)
t3 = Rectangle(a=4,b=5)
print(t1)
print(t2)
print(t3)

