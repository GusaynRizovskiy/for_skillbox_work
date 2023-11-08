from typing import Callable,Any
def func_1(x: int) -> int:
    return x + 10
def func_2(func_1: Callable,*args) -> Any:
    result1 = func_1(*args)
    print("Результат {}".format(result1*result1))
    return result1

work = func_2(func_1,9)