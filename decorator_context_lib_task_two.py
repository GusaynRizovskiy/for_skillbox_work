import time
from collections.abc import Iterator
from contextlib import contextmanager

# class Timer():
#     def __init__(self):
#         print("Время работы кода")
#         self.start = None
#     def __enter__(self):
#         self.start = time.time()
#         return self
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(time.time()-self.start)
#         return True
@contextmanager
def timer():
    start = time.time()
    try:
        yield
    finally:
        print(time.time()-start)

with timer() as t:
    print("Первая часть")
    k = 100**200*4**2000000
with timer() as t:
    print("Вторая часть")
    l = 200*200**1000000
with timer() as t:
    print("Третья часть")
    m = 100**200*4**2222222
