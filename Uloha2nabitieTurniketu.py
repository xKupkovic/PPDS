from time import sleep
from random import randint
from fei.ppds import Thread, Mutex, Semaphore
from fei.ppds import print
 
 
def rendezvous(thread_name):
    sleep(randint(1,10)/10)
    print('rendezvous: %s' % thread_name)
 
 
def ko(thread_name):
    print('ko: %s' % thread_name)
    sleep(randint(1,10)/10)
 
 
def barrier_example(thread_name):
    global t1,t2,m,count,N
    while True:
        rendezvous(thread_name)
        m.lock()
        count+=1
        if(count == N):
            t1.signal(N)
        m.unlock()
        t1.wait()
        ko(thread_name)
        m.lock()
        count-=1
        if(count == 0):
            t1.signal(N)
        m.unlock()
        t1.wait()
        
t1 = Semaphore(0)
t2 = Semaphore(0)
m = Mutex()
count = 0

N = 5 
 
threads = list()
for i in range(5):
    t = Thread(barrier_example, 'Thread %d' % i)
    threads.append(t)
 
for t in threads:
    t.join()
