# PPDS

Program 1

This program concurently increments counter in shared class and increments element of id counter by one. For this to work properly i had to use lock before incementation of counter and also element. This is the very least instructions program needs to have lock on to function all of the time.

Program 2

This program concurently sets only element. Incrementation of counter is locked, therefore it can only be called by one thread at the time. With this type of lock there are few errors. First one is accessing element that is out of range. Second one is multiple incrementations of element in array. This is due to multiple threads beeing at same counter at once therefore multiple times incrementing same element.


