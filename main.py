from time import sleep
from random import randint
from fei.ppds import Thread, Mutex, Semaphore, print

#Number of savages
N = 10
#Number of meals
M = 3
#Number of cooks
C = 5


class Shared:
    def __init__(self, m):
        """
        Shared data for threads
        :param m: number of meals
        """
        self.servings = m
        self.mutex = Mutex()
        self.empty_pot = Semaphore(0)
        self.full_pot = Semaphore(0)
        self.barrier = SimpleBarrier(C)

class SimpleBarrier:
    def __init__(self, n):
        """
        Initalize Simple barrier with number of iterations
        :param n: number of iterations
        """
        self.n = n
        self.count = 0
        self.mutex = Mutex()
        self.barrier = Semaphore(0)

    def wait(self, callback=None, callback_params=[], each=None, last=None):
        """
        Add waiting thread to barrier
        :param callback_params: parameters for function on last
        :param callback: function to call on last
        :param each: string printed for each
        :param last: string printed for last
        :return: NONE
        """
        self.mutex.lock()
        self.count += 1
        if each:
            print(each)
        if self.count == self.n:
            if last:
                print(last)
            if callback is not None:
                callback(*callback_params)
            self.count = 0
            self.barrier.signal(self.n)
        self.mutex.unlock()
        self.barrier.wait()

def savage(i, shared):
    pass

def cook(i,shared):
    pass

def main():
    """
        Main function that initalizes data and threads and run them.
        :return: NONE
        """
    shared = Shared(0)
    threads = []
    for i in range(N):
        threads.append(Thread(savage, i, shared))
    for j in range(C):
        threads.append(Thread(cook, j, shared))

    for t in threads:
        t.join()


if __name__ == '__main__':
    main()
