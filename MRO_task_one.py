class Robot():
    def __init__(self,model: str) ->None:
        self.model = model
    def answer(self) -> None:
        print("Я робота")
class Fligth():
    def __init__(self,high:int,speed:int) -> None:
        self.high = high
        self.speed = speed
    def fly(self) -> None:
        print("Совершаю пилотирование в воздухе")
    def get_up(self) -> None:
        print("Взлетаю")
    def get_down(self) -> None:
        print("Приземляюсь")
class Raptor_robot(Robot,Fligth):
    def __init__(self,model:str,high:int,speed:int) ->None:
        super().__init__(model,high,speed)
    def operate(self) -> None:
        print("Веду разведку с воздуха")
    def fly(self) -> None:
        super(Raptor_robot,self).fly()
class Military_Robot(Fligth,Robot):
    def __init__(self,model:int,high:int,speed:int,weapon:str) -> None:
        super().__init__(model,high,speed)
        self.weapon = weapon
    def operate(self) -> None:
        print("Веду защиту военного объекта")

robot_raptor_one = Raptor_robot(2070,70,200)
robot_raptor_one.operate()
robot_raptor_one.fly()
robot_military_one = Military_Robot(2071,90,400,"laser")
robot_military_one.operate()

