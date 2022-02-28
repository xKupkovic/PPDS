from time import sleep
from random import randint
from fei.ppds import Thread, Mutex, Event
from fei.ppds import print

class SimpleBarrier:
    def __init__(self, N):
        self.N = N
        self.C = 0
        self.M = Mutex()
        self.T = Event()
        pass
 
    def wait(self):
        self.M.lock()
        self.C += 1
        if(self.C==self.N):
            self.C = 0
            self.T.signal()
        self.M.unlock()
        self.T.wait()
        self.T.clear()
        pass
 
def rendezvous(thread_name):
    sleep(randint(1,10)/10)
    print('rendezvous: %s' % thread_name)
 
 
def ko(thread_name):
    print('ko: %s' % thread_name)
    sleep(randint(1,10)/10)
 
 
def barrier_example(thread_name):
    while True:
        rendezvous(thread_name)
        ko(thread_name)

sb1 = SimpleBarrier(5)
sb2 = SimpleBarrier(5)
 
threads = list()
for i in range(5):
    t = Thread(barrier_example, 'Thread %d' % i)
    threads.append(t)
 
for t in threads:
    t.join()
