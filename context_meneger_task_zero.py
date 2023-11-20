import time
class Timer:
    def __init__(self) -> None:
        print("Время работы кода ")
        self.start = None
    def __enter__(self) -> 'Timer':
        self.start = time.time()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(time.time() - self.start)
with Timer() as t1:
    print("Первая часть выполняется ")
    al = 10 * 20 **1000000
with Timer() as t1:
    print("Вторая часть выполняется ")
    at = 20 * 40 ** 40000
with Timer() as t1:
    print("Третья часть выполняется ")
    ak = 13 * 40 ** 300000
