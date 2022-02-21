from fei.ppds import Thread,Mutex
from collections import Counter
 
class Shared():   
    pass
 
 
def fnc_test(shared): 
    pass
 
 
mutex = Mutex()
shared = Shared(1_000_000)
 

t1 = Thread(fnc_test, shared,mutex)
t2 = Thread(fnc_test, shared,mutex)


t1.join()
t2.join()



c = Counter(shared.elms)
print(c.most_common())
