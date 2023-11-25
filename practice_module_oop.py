class Property():
    """
    Базовый класс Property
    :arg worth - цена
    :method - nalog
    """
    def __init__(self,worth) -> None:
        self.__worth = worth
    def get_worth(self):
        return self.__worth
    def nalog(self):
        pass
class Apartament(Property):
    def __init__(self,worth) -> None:
        super().__init__(worth)
    def nalog(self):
        return self.get_worth()/1000
    def __str__(self):
        return "Налог на квартиру: {}".format(self.nalog())
class Car(Property):
    def __init__(self,worth) -> None:
        super().__init__(worth)
    def nalog(self) -> float:
        return self.get_worth()/200
    def __str__(self):
        return "Налог на машину: {}".format(self.nalog())
class Country_House(Property):
    def __init__(self,worth) -> None:
        super().__init__(worth)
    def nalog(self) -> float:
        return self.get_worth()/500
    def __str__(self):
        return "Налог на дачу: {}".format(self.nalog())
money = float(input("Сколько у вас денег: "))
cost = float(input("Стоимость вашего имущества: "))
imuchestvo_house = Apartament(cost)
imuchestvo_car = Car(cost)
imuchestvo_house_country = Country_House(cost)
print(imuchestvo_house)
print(imuchestvo_car)
print(imuchestvo_house_country)
sum_nalog = imuchestvo_house.nalog() + imuchestvo_car.nalog() + imuchestvo_house_country.nalog()
if sum_nalog > money:
    print("Вам не хватает",money-sum_nalog)



