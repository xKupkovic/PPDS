from time import sleep
from random import randint
from fei.ppds import Mutex, Semaphore, Thread, print

class Shared:
    def __init__(self, N):
        self.finished = False
        self.mutex = Mutex()
        self.free = Semaphore(N)
        self.items = Semaphore(0)

def producer():
    pass

def consumer():
    pass

s = Shared(10)
c = [Thread(consumer, s) for _ in range(2)]
p = [Thread(producer, s) for _ in range(2)]

[t.join() for t in c+p]
