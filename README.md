# PPDS

#Uloha 1

In the beginning the barrier initialize with fixed number of threads. Barrier works with events that means that every thread that runs wait function increment counter by 1 and when counter reaches value of number of threads then with signal all other threads are released and program can continue. O