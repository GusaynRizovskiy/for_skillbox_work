class Point():
    def __init__(self,x = 0, y = 0) -> None:
        self.__x = x
        self.__y = y
    def get_x(self) -> int:
        return self.__x
    def get_y(self) -> int:
        return self.__y
    def set_x(self,x) -> None:
        if x == int:
            self.__x = x
        else:
            raise Exception("Должно передаваться число")
    def set_y(self,y) -> None:
        if y == int:
            self.__y = y
        else:
            raise Exception("Должно передаваться число")
    def __str__(self) -> str:
        return "Координаты точки: ({x},{y})".format(x = self.__x,y=self.__y)
p1 = Point(3,4)
print(p1)
p2 = Point(5,6)
print(p2)
print(p1.get_y())
print(p2.get_x())
p1.set_x(8)