from time import sleep
from random import randint
from fei.ppds import Mutex, Semaphore, Thread, print

class Shared:
    def __init__(self, N):
        self.finished = False
        self.mutex = Mutex()
        self.free = Semaphore(N)
        self.items = Semaphore(0)
