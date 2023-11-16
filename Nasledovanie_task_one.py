class Ship():
    def __init__(self,model: int) -> None:
        self.__model = model
    def __str__(self):
        return "Моя модель номер {}".format(self.__model)
    def swim(self):
        print("Плыву по воде")
class War_Ship(Ship):
    def __init__(self,model: int, weapon: str) -> None:
        super().__init__(model)
        self.weapon = weapon
    def attack(self):
        print("Атакую вражеский корабль своим оружием:", self.weapon)
    def __str__(self):
        return "У меня есть отличное оружие {}".format(self.weapon)
class Gruz_SHip(Ship):
    def __init__(self,model:int) -> None:
        super().__init__(model)
        self.zapolnennosty = 0
    def vigruzka(self):
        self.zapolnennosty-=1
    def zagruzka(self):
        self.zapolnennosty+=1
    def __str__(self):
        return "Заполненность корабля составляет: {}".format(self.zapolnennosty)

ship_one = Ship(234)
print(ship_one)
print("\n")
war_ship_one = War_Ship(2070, "laser")
print(war_ship_one)