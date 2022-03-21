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
    """
        Function simulate savages eating from pot, it waits for it to get filled by cooks when empty
        :param i: identifier for savage
        :param shared: shared data for threads
        :return: NONE
        """
    sleep(randint(1, 100) / 100)
    while True:
        shared.mutex.lock()
        if shared.servings == 0:
            shared.empty_pot.signal(C)
            shared.full_pot.wait()
        print(f'savage {i}: take from pot')
        shared.servings -= 1
        shared.mutex.unlock()
        sleep(randint(20, 50) / 100)

def fill_pot(shared):
    """
    Sets servings in shared data and signals full pot
    :param shared: shared data for threads
    :return: None
    """
    shared.servings = M
    shared.full_pot.signal()


def cook(i, shared):
    """
    Waits until pot is empty, after that cooks servings until maximum is reached, after it signals savages
    :param i: identifier for cook
    :param shared: shared data fro threads
    :return: NONE
    """
    while True:
        shared.empty_pot.wait()
        sleep(randint(50, 200) / 100)
        shared.barrier.wait(callback=fill_pot, callback_params=[shared], each="cook {} is cooking".format(i),
                            last="cook {} finished cooking".format(i))


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
