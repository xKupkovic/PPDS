"""
Author: Jakub Kupkovic
Date: 21.4.2022

Description: Program runs sync and async tasks and compares speeds
"""

from time import sleep

async def async_task(name,work_queue):
    """
    Async task that sleeps for given time
    :param name: name of worker
    :param work_queue: tasks to do
    """
    while not work_queue.empty():
        time = work_queue.get()
        print(f"Async task {name} starting")
        sleep(time)
        print(f"Async task {name} finished")
    pass

def sync_task(name,work_queue):
    """
    Synchronous task that sleeps for given time
    :param name: name of worker
    :param work_queue: tasks to do
    """
    pass

def main():
    pass


if __name__ == "__main__":
    main()