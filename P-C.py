from time import sleep
from random import randint
from fei.ppds import Mutex, Semaphore, Thread, print

class Shared:
    def __init__(self, N):
        self.finished = False
        self.mutex = Mutex()
        self.free = Semaphore(N)
        self.items = Semaphore(0)

def producer(shared):
    while(not shared.finished):
        shared.free.wait()
        shared.mutex.lock()
        sleep(randint(1, 10) / 100)
        shared.mutex.unlock()
        shared.items.signal()
    pass

def consumer(shared):
    while(not shared.finished):
        shared.items.wait()
        shared.mutex.lock()
        sleep(randint(1, 10) / 100)
        shared.mutex.unlock()
        sleep(randint(1, 10) / 10)
    pass

def main_loop():
    average_times = []
    for i in range(10):
        s = Shared(10)
        c = [Thread(consumer, s) for _ in range(2)]
        p = [Thread(producer, s) for _ in range(2)]
        [t.join() for t in c+p]
        sleep(5)
        s.finished = True

main_loop()     
        

