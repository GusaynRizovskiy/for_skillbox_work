import random

def generator():
    i = 0
    while True:
        i+=1
        yield i
generator()