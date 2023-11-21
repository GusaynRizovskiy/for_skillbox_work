import abc
from abc import ABC,abstractmethod
class Transport(ABC):
    def __init__(self,colour:str,speed:int) -> None:
        self._colour = colour
        self._speed = speed
    def move(self):
        print("Я двигаюсь по ")
    def music(self):
        print("Воспроизвожу музыку")
    @property
    def colour(self):
        return self._colour
    @property
    def speed(self):
        return self._speed
    @colour.setter
    def colour(self,new_colour):
        self._colour = new_colour
    @speed.setter
    def set_speed(self,new_speed):
        self._speed = new_speed
class Music:
    def play(self):
        print("Ясаул ясаул, что ж ты продал коня, пристелить не поднялась рука...")
class auto(Transport,Music):
    def __init__(self,colour:str,speed:int) -> None:
        super().__init__(colour,speed)
        print("только по земле")
class boat(Transport,Music):
    def __init__(self,color:str,speed:int)-> None:
        super().__init__(color,speed)
        Transport.move()
        print("только по воде")
        Music.play()
class Amfibi(Transport,Music):
    def __init__(self,color: str, speed: int) -> None:
        super().__init__(color,speed)
        Transport.move()
        print("и по воде, и по земле")
        Music.play()
t1 = auto("red", 160)
t2 = boat("green", 130)
t3 = Amfibi("black",700 )