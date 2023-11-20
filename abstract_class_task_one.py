import abc
from abc import ABC,abstractmethod
class Transport(ABC):
    def __init__(self,colour:str,speed:int) -> None:
        self.colour = colour
        self.speed = speed
    def move(self):
        print("Я двигаюсь по ")
    def music(self):
        print("Воспроизвожу музыку")
class Music:
    def play(self):
        print("Ясаул ясаул, что ж ты продал коня, пристелить не поднялась рука...")
class auto(Transport,Music):
    def __init__(self,colour:str,speed:int) -> None:
        super().__init__(colour,speed)
        Transport.move()
        print("только по земле")
        Music.play()
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