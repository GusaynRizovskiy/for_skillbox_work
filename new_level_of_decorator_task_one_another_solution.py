from typing import Callable
def ingridient(func: Callable) ->Callable:
    def wrapped_func(*args,**kwargs):
        print("#помидоры#")
        func(*args,**kwargs)
        print("~салат~")
        return func
    return wrapped_func
def get_some_bans(func:Callable) ->Callable:
    def wrapped_func(*args,**kwargs):
        print("</-----------\>")
        func(*args,**kwargs)
        print("<\____________/>")
        return func
    return wrapped_func
@get_some_bans
@ingridient
def filling_burger(filler):
    print(filler)
filling_burger("ветчина")