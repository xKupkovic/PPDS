# PPDS

#Task 1

In the beginning the barrier initialize with fixed number of threads. Barrier works with events that means that every thread that runs wait function increment counter by 1 and when counter reaches value of number of threads then with signal all other threads are released and program can continue. It also clears it self when threads are released.

#Task 2

This task consists of 3 separete programs. Each one is little different implementation of the other.

First implementation implements 2 phase barrier, it runs first function on all threads and then wait for them on first semaphore. When the last thread is finished it waits for second semaphore(which should be set by previous run) and signals first one to release. After that second function can be ran. There it is the same as first part but with inverted semaphores. For it to run,on first intialization second semaphore must have signal set, so it won't get stuck on when last thread is finished.

Second implementation implements loading of tourniquet. Here we utilise multi signalization or loading of torniquet. Here we dont need 2 semaphores. On each part when all threads are finished, tourniquet loads number of threads of signals and release them all. 

Third implementation is easiest. In this one we utilise Simplle barrier from previous task. This barrier use wait function after each part in program so it can continue only after all threads have got to the barrier.