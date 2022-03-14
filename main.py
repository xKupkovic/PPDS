from random import randint
from time import sleep
from fei.ppds import Thread, Semaphore, print, Event, Mutex

class SharedData:
    def __init__(self):
        self.ad = Semaphore(1)
        self.ts = Semaphore(1)
        self.vd = Event()

class LS:
    def __init__(self):
        self.m = Mutex()
        self.c = 0

    def lock(self, sem):
        self.m.lock()
        self.c += 1
        if self.c == 1:
            sem.wait()

        self.m.unlock()
        return self.c

    def unlock(self, sem):
        self.m.lock()
        self.counter -= 1
        if self.counter == 0:
            sem.signal()

        self.mutex.unlock()
