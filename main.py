"""
Author: Jakub Kupkovic
Date: 21.4.2022

Description: Program runs sync and async tasks and compares speeds
"""

from time import sleep,time
from asyncio import Queue as aq
from asyncio import gather
from queue import Queue as sq

async def async_task(name,work_queue):
    """
    Async task that sleeps for given time
    :param name: name of worker
    :param work_queue: tasks to do
    """
    while not work_queue.empty():
        t = work_queue.get()
        print(f"Async task {name} starting")
        sleep(t)
        print(f"Async task {name} finished")
    pass

def sync_task(name,work_queue):
    """
    Synchronous task that sleeps for given time
    :param name: name of worker
    :param work_queue: tasks to do
    """
    while not work_queue.empty():
        t = work_queue.get()
        print(f"Synchronous task {name} starting")
        sleep(t)
        print(f"Synchronous task {name} finished")
        yield
    pass

def main():

    times = [0.5, 4, 2, 3, 8]
    async_q = aq()
    sync_q = sq()
    for t in times:
        async_q.put(t)
        sync_q.put(t)

    start_time = time()
    print("Starting async queue")
    #RUN async
    print(f"Async tasks finished with time {time()-start_time}")

    start_time = time()
    print("Starting sync queue")
    #RUN sync
    print(f"Sync tasks finished with time {time()-start_time}")
    pass


if __name__ == "__main__":
    main()