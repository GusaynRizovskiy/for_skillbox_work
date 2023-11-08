import time
from typing import Any, Callable
def timer(func: Callable) -> Callable:
    def wrapped_func(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        finish_result = round(end - start,4)
        print("Функция проработа {} секунд".format(finish_result))
        return result
    return wrapped_func
@timer
def squares_sum() -> int:
    number = 100
    result = 0
    for _ in range(number+1):
        result += sum([i**2 for i in range(10000)])
    return result
@timer
def cubes_sum(number: int) -> int:
    result = 0
    for _ in range(number+1):
        result += sum([i**3 for i in range(10000)])
    return result

print(squares_sum())
print(cubes_sum(200))
