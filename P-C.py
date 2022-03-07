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
    plt_x=[]
    plt_y=[]
    avg_produced = []
    avg_consumed = []
    for x in range(1,11):
        for y in range(1,11):
            plt_x.append(x)
            plt_y.append(y)
            produced = []
            consumed = []
            for i in range(10):
                s = Shared(10)
                c = [Thread(consumer, s) for j in range(x)]
                p = [Thread(producer, s) for j in range(y)]
                sleep(0.1)
                s.finished = True
                produced.append(s.produced)
                consumed.append(s.consumed)
                s.free.signal(100)
                s.items.signal(100)
                [t.join() for t in c+p]
            avg_produced.append(sum(produced)/10)
            avg_consumed.append(sum(consumed)/10)

    fig = plt.figure(1)
    plt.title('average produced')
    plt.xlabel('consumer')
    plt.ylabel('producer')
    ax= plt.axes(projection = '3d')
    ax.scatter(plt_x, plt_y, avg_produced, c=avg_produced, cmap='viridis', linewidth=2)
    figb = plt.figure(2)
    plt.title('average consumed')
    plt.xlabel('consumer')
    plt.ylabel('producer')
    ay= plt.axes(projection = '3d')
    ay.scatter(plt_x, plt_y, avg_consumed, c=avg_produced, cmap='viridis', linewidth=2)
    fig.show()
    figb.show()

main_loop()     
        

