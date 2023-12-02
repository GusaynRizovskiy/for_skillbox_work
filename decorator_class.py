import functools
from typing import Callable
import time
from datetime import datetime
def clas_time(cls):
    @functools.wraps(cls)
    def wraped(*args,**kwargs):
        instanse = cls(*args,**kwargs)
        print("Время создания инстанса: ",datetime.utcnow())
        return instanse
    return wraped
def timer(func:Callable)->Callable:
    @functools.wraps(func)
    def wraped(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        stop = time.time()
        print("Время выполнения функции: ",stop-start)
        return result
    return wraped
def for_all_class(decorator: Callable) -> Callable:
    @functools.wraps(decorator)
    def decorate(cls):
        for elem in dir(cls):
            if elem.startswith("__") is False:
                cur_decor = getattr(cls,elem)
                decorated_method = decorator(cur_decor)
                setattr(cls,elem,decorated_method)
        return cls
    return decorate
@clas_time
@for_all_class(timer)
class Functions:
    def __init__(self,max_num:int)-> None:
        self.max_num = max_num
    @timer
    def squares_sum(self)->int:
        number = 100
        result = 0
        for _ in range(number+1):
            result+= sum([elem**2 for elem in range(self.max_num)])
        return result
    @timer
    def cubes_sum(self, number:int)->int:
        result = 0
        for _ in range(number+1):
            result+=sum([elem**3 for elem in range(self.max_num)])
        return result

myfunc1 = Functions(max_num=1000)
