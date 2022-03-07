from time import sleep
from random import randint
from fei.ppds import Mutex, Semaphore, Thread, print
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

class Shared:
    def __init__(self, N):
        self.finished = False
        self.mutex = Mutex()
        self.free = Semaphore(N)
        self.items = Semaphore(0)
        self.consumed = 0
        self.produced = 0

def producer(shared):
    while(not shared.finished):
        sleep(randint(1, 10) / 100)
        shared.free.wait()
        shared.mutex.lock()
        sleep(randint(1, 10) / 1000)
        shared.produced +=1
        shared.mutex.unlock()
        shared.items.signal()
    pass

def consumer(shared):
    while(not shared.finished):
        shared.items.wait()
        shared.mutex.lock()
        sleep(randint(1, 10) / 1000)
        shared.consumed +=1
        shared.mutex.unlock()
        sleep(randint(1, 10) / 100)
    pass

def main_loop():
    s = Shared(10)
    c = [Thread(consumer, s) for j in range(6)]
    p = [Thread(producer, s) for j in range(4)]
    sleep(0.1)
    s.finished = True
    s.free.signal(100)
    s.items.signal(100)
    [t.join() for t in c+p]


main_loop()     
        

