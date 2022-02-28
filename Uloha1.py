from random import randint
from time import sleep
from fei.ppds import Thread, Event, Mutex 
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
 
def before_barrier(thread_id):
    print("vlakno %d pred barierou" % thread_id)
def after_barrier(thread_id)
    print("vlakno %d po bariere" % thread_id)
 
def barrier_cycle(barrier, thread_id):
    while True:
        before_barrier(thread_id)
        barrier.wait()
        after_barrier(thread_id)
        barrier.wait()
 
 
sb = SimpleBarrier(5)

threads = [Thread(barrier_example,sb,i) for i in range(5)]
[t.join() for t in threads]

