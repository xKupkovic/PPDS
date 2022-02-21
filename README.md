# PPDS

Programs used, all have same base with main program that creates threads and start execution of counter concurently. All programs have same data and same array size. By increasing array size but we can get rid of out of bounds error in following programs but It is only band aid to this problem, not a solution.

Program 1

This program concurently increments counter in shared class and increments element of id counter by one. For this to work properly i had to use lock before incementation of counter and also element. This is the very least instructions program needs to have lock on to function all of the time.

Program 2

This program concurently sets only element. Incrementation of counter is locked, therefore it can only be called by one thread at the time. With this type of lock there are few errors. First one is accessing element that is out of range. Second one is multiple incrementations of element in array. This is due to multiple threads beeing at same counter at once therefore multiple times incrementing same element.

Program 3

This program concurently increments counter. Incrementation of element is happening only on one thread at the same time.  There are also same errors like on previous program. However there difference on how often which one happens. Out of bounds error is not happening more often but multiple of same element incrementations happen rarely.

Conclusion

By placing lock to different parts of program can alter the way the program behaves. By experimenting with placement we got different results.