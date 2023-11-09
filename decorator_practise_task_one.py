from typing import Callable
def how_are_you(func:Callable) -> Callable:
    def wrapped_function():
        answer = input("Как дела?")
        print("А у меня не очень, ладно держи свою фунцию")
        return func
    return wrapped_function()
@how_are_you
def test():
    print('<Тут что-то происходит...>')


test()