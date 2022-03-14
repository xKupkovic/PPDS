from random import randint
from time import sleep
from fei.ppds import Thread, Semaphore, print, Event, Mutex

class SharedData:
    def __init__(self):
        self.ad = Semaphore(1)
        self.ts = Semaphore(1)
        self.vd = Event()
