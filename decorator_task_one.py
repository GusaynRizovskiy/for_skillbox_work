from typing import Callable,Any
def decorator(func:Callable) -> Callable:
    def wrapped_function(*args):
        result = func(*args)
        result = func(*args)
        return result
    return wrapped_function
@decorator
def greeting(name:str) -> None:
    print('Привет, {name}!'.format(name=name))

greeting('Tom')