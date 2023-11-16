class Robot():
    def __init__(self,model) -> None:
        self.model = model
    def __str__(self) -> str:
        return "Моя модель {} ".format(self.model)

class Robot_pilisos(Robot):
    def __init__(self,model:int) -> None:
        super().__init__(model)
        self.place_of_mesok = 0
    def operate(self):
        self.place_of_mesok+=1
        print(super().__str__() + "Я пылесошу, заполненость мешка: ", self.place_of_mesok)
class Military_Robot(Robot):
    def __init__(self,model: int,weapon:str)-> None:
        super().__init__(model)
        self.weapon = weapon
    def operate(self):
        print("Провожу защиту военного объекта с помощью ", self.weapon,",", super().__str__())
class under_water_robot(Military_Robot):
    def __init__(self,model:int,weapon:str, deep:int) -> None:
        super().__init__(model,weapon)
        self.deep = deep
    def operate(self):
        print("Провожу защиту военного объекта под водой на глубине",self.deep," c помощью", self.weapon, super().__str__())
rob_one = Robot_pilisos(2300)
rob_one.operate()
rob_one.operate()
rob_two = Military_Robot(2700,"laser")
rob_two.operate()
rob_three = under_water_robot(3700,"pulemet",30)
rob_three.operate()
