# PPDS

## Async program

Program is divided into 2 parts.
First part is setup and second part is task.
In setup we create 2 async tasks to execute sleep command with time.
Each run prints information. 
Every time async task is finished, new one starts.
Await is on sleep()


## Synchronous program

As with Asynchronous program, this one is also divided into 2 parts.
It is almost exactly like program before but instead of async task there are generators.
Each generator runs sleep command with given time. Generators run one after another.
Yield function is on sleep().

## Comparison

Asynchronous program was faster. With 20 runs average improvement was by 30%.
This may be because there was no overhead in async program with synchronisation.
