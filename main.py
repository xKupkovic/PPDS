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

def cart():
    while True:
        #Load
        #BoardQ signal
        #boarded Wait
        #Run
        #unlaod()
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
