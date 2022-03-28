"""
Author: Jakub Kupkovic

Date: 28.3.2021

Desc:
    Program simulates problem of the rollercoaster.

"""

from time import sleep
from random import randint
from fei.ppds import Thread, Mutex, Semaphore, print, Event


class Shared:
    def __init__(self, M, C):
        """
        Shared data for threads
        :param M: number of Trains
        :param C: number of people
        """
        self.M = M
        self.C = C
        self.boarding_areas = [Semaphore(0) for i in range(M)]
        self.unloading_area = [Semaphore(0) for i in range(M)]
        self.board_queue = Semaphore(0)
        self.board_b = SimpleBarrier(C)
        self.boarded = Semaphore(0)
        self.unboard_queue = Semaphore(0)
        self.unboard_b = SimpleBarrier(C)
        self.unboarded = Semaphore(0)
        pass
    def get_next(self,i):
        i = (i + 1) % self.M
        return i

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


def load(id):
    """
    Prints out when cart has been loaded
    :param id: cart id
    """
    sleep(randint(10,30)/1000)
    print("Cart {} has loaded".format(id))

def run(id):
    """
    Prints out when cart has ran
    :param id: cart id
    """
    sleep(randint(20, 80) / 1000)
    print("Cart {} has ran".format(id))

def unload(id):
    """
    Prints out when cart has been unloaded
    :param id: cart id
    """
    sleep(randint(10, 30) / 1000)
    print("Cart {} has unloaded".format(id))

def board(id):
    """
    Prints out when person has boarded
    :param id: person id
    """
    sleep(randint(10, 20) / 1000)
    print("Person {} has boarded".format(id))

def unboard(id):
    """
    Prints out when person has unboarded
    :param id: person id
    """
    sleep(randint(10, 20) / 1000)
    print("Person {} has unboarded".format(id))

def cart(id,shared,capacity):
    """
    Simulates cart
    :param id: cart id
    :param shared: shared data
    """
    while True:
        shared.boarding_areas[id].wait()
        load(id)
        shared.board_queue.signal(capacity)
        shared.boarded.wait()
        shared.boarding_areas[shared.get_next(id)].signal()
        run(id)
        shared.unloading_area[id].wait()
        unload(id)
        shared.unboard_queue.signal(capacity)
        shared.unboarded.wait()
        shared.unloading_area[shared.get_next(id)].wait()
        pass
    pass


def passenger(id, shared):
    while True:
        shared.board_queue.wait()
        board(id)
        shared.board_b(callback=shared.boarded.signal)
        shared.unboard_queue.wait()
        unboard(id)
        shared.unboard_b.wait(callback=shared.unboarded.signal)
        pass
    pass


def main():
    """
        Main function that initalizes data and threads and run them.
        :return: NONE
        """
    M,C = 5,20
    shared = Shared(M,C)
    threads = []

    for i in range(M):
        threads.append(Thread(cart(i,shared)))
    for i in range(C):
        threads.append(Thread(passenger(i,shared)))

    for t in threads:
        t.join()


if __name__ == '__main__':
    main()
