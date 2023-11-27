from collections.abc import  Iterator
from contextlib import contextmanager
@contextmanager
def func(num: int) -> Iterator[int]:
    print("Входим в функцию")
    try:
        yield num+1
    except ZeroDivisionError as zer:
        print("Получена ошибка", zer)
    finally:
        print("Мир вам суки")

with func(-1) as w:
    print("Наше полученное число:",w)
    print(w/0)