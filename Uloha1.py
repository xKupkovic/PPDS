from random import randint
from time import sleep
from fei.ppds import Thread, Event, Mutex 
from fei.ppds import print
 
 
class SimpleBarrier:
    def __init__(self, N):
        pass
 
    def wait(self):
        pass
 
 
def barrier_example(barrier, thread_id):
    """Predpokladajme, ze nas program vytvara a spusta 5 vlakien,
    ktore vykonavaju nasledovnu funkciu, ktorej argumentom je
    zdielany objekt jednoduchej bariery
    """
    sleep(randint(1,10)/10)
    print("vlakno %d pred barierou" % thread_id)
    barrier.wait()
    print("vlakno %d po bariere" % thread_id)
 
 
sb = SimpleBarrier(5)


for i in range(5):
    t = Thread(barrier_example(sb,i))
