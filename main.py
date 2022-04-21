"""
Author: Jakub Kupkovic
Date: 21.4.2022

Description: Program runs sync and async tasks and compares speeds
"""
import asyncio
from time import sleep,time
from asyncio import Queue as aq
from asyncio import gather
from queue import Queue as sq


async def async_task(name, work_queue):
    """
    Async task that sleeps for given time
    :param name: name of worker
    :param work_queue: tasks to do
    """
    while not work_queue.empty():
        t = await work_queue.get()
        print(f"Async task {name} starting")
        await asyncio.sleep(t)
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


async def async_handler(times):
    """
    Function handles async tasks
    :param times: execution times
    """
    async_q = aq()
    for t in times:
        await async_q.put(t)
    await gather(
        async_task("One", async_q),
        async_task("Two", async_q)
    )


def sync_handler(times):
    """
    Handles generators of sync tasks
    :param times: execution times
    """
    sync_q = sq()
    for t in times:
        sync_q.put(t)
    tasks = [
        sync_task("One", sync_q),
        sync_task("Two", sync_q)
    ]
    done = False
    while not done:
        for t in tasks:
            try:
                next(t)
            except StopIteration:
                tasks.remove(t)
            if len(tasks) == 0:
                done = True


def main():

    times = [0.5, 4, 2, 3, 8]

    start_time = time()
    print("Starting async queue")
    asyncio.run(async_handler(times))
    print(f"Async tasks finished with time {time()-start_time}")

    start_time = time()
    print("Starting sync queue")
    sync_handler(times)
    print(f"Sync tasks finished with time {time()-start_time}")
    pass


if __name__ == "__main__":
    main()