from fei.ppds import Thread,Mutex
from collections import Counter
 
class Shared():
    def __init__(self,size):
        self.elms = [0]*size
        self.end = size
        self.counter =0
    pass
 
#Incrementation method with mutex
def fnc_increment(shared,mutex):
    while(True):
        if(shared.counter >= shared.end):
            break
        mutex.lock()
        shared.elms[shared.counter] += 1
        shared.counter+=1
        mutex.unlock()   
    pass
 
 
mutex = Mutex()
shared = Shared(1_000_000)
 
t1 = Thread(fnc_increment, shared,mutex)
t2 = Thread(fnc_increment, shared,mutex)

t1.join()
t2.join()

c = Counter(shared.elms)
print(c.most_common())
