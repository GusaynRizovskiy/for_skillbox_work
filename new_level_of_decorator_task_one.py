from typing import Callable
def xleb(func:Callable) -> Callable:
    print("Хлеб")
    return func
def ingridien(func:Callable) -> Callable:
    print("Салат,помидоры")
    return func
@ingridien
@xleb
def sandvich(ingridient:str):
    return "Начинку сэндвича составляют {}".format(ingridient)

print(sandvich("Индейка"))