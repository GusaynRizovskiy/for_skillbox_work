from abc import ABC,abstractmethod
class Figure(ABC):
    def __init__(self,x:int,y:int,length:int,size) -> None:
        self.x = x
        self.y = y
        self.lenght = length
        self.size =size
    def move(self,x: int, y: int) -> None:
        self.x = x
        self.y = y
class SizeMixin:
    def resize(self,length: int,widht:int):
        self.lenght = length
        self.width = widht
class Square(Figure,SizeMixin):
    def __init__(self,x: int,y: int,length: int,widht: int) -> None:
        super().__init__(x,y,length,widht)
class Rectangle(Figure, SizeMixin):
    def __init__(self,x: int,y: int,length: int,widht: int) -> None:
        super().__init__(x,y,length,widht)
t1 = Square(2,2,6,6)
t2 = Rectangle(6,6,18,9)
for fugure in [t1,t2]:
    length = fugure.x * 2
    width = fugure.y * 2
    fugure.resize(length,width)

