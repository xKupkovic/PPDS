from fei.ppds import Mutex,print,Semaphor,Thread

def get_next_fibonacci():
    pass

def fibonacci_cycle():
    pass
    
THREADS_NUMBER = 5

nums = []

nums.append(0)
nums.append(1)

threads = [ Thread(fibonacci_cycle) for i in range(THREADS_NUMBER)]
[t.join() for t in threads]

