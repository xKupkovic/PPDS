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
    def __init__(self, M):
        """
        Shared data for threads
        :param M: number of Trains
        """
        self.M = M
        self.C = 0
        self.boarding_areas = [Semaphore(0) for i in range(M)]
        self.unloading_area = [Semaphore(0) for i in range(M)]
        self.board_queue = Semaphore(0)
        self.boarded = Event()
        self.unboard_queue = Semaphore(0)
        self.unboarded = Event()
        pass

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

def cart(id,shared):
    """
    Simulates cart
    :param id: cart id
    :param shared: shared data
    """
    while True:
        load(id)
        #Load
        #BoardQ signal
        #boarded Wait
        run(id)
        unload(id)
        #unboardQ signal
        #unboarded.wait
        pass
    pass


def passenger():
    while True:
        #BoardQ wait
        #board
        #BoardB wait
        #unboardQWait
        #unboard
        #unboardBWait
        pass
    pass


def main():
    """
        Main function that initalizes data and threads and run them.
        :return: NONE
        """
    shared = Shared(0)
    threads = []


    for t in threads:
        t.join()


if __name__ == '__main__':
    main()
