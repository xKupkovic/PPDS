# PPDS

## Initialization

Before anything I had to check if I have enabled CUDA on my computer.
This for checked with 
``` python
from numba import cuda
print(cuda.gpus)
```

## Bruteforce search

The problem I chose is brute force searching for key vector that is solution to bit matrix.

First I initialized random bit matrix, and then I initialized random solution vector.
Then I initialized another matrices that I used later.
First matrix had all the cached values from operations inside block. Second was for storing results.

### Kernel program

Kernel program was composed of 3 parts. 

First part is executed by 128 threads and that is xoring input vector with matrix.
Result is then stored in cached matrix.
After that there is syncpoint to wait for all threads in block.

Second part consists of summing all the bits in row.
This is executed only by 16 threads (1 for each row).
If x value of thread is not equal to 0 then skip.
Final sum modulo 2 is stored then in next column of cached matrix.
There is another syncpoint.

Last part is to check for solution.
I was unable to use more than 1 thread in this part.

### Results

After program ran with matrix (16x16) the last result found is then copied from device.
The result is then printed out.
Brute force searched for 65536 vectors in instant with this paralelisation.
