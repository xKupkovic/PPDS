from fei.ppds import Mutex,print,Semaphor,Thread

def get_next_fibonacci(i):
    global nums
    return nums[i-2]+nums[i-1]
    pass

def fibonacci_cycle():
    count = 2
    while True:
        
    pass
    
THREADS_NUMBER = 5

nums = []

nums.append(0)
nums.append(1)

threads = [ Thread(fibonacci_cycle) for i in range(THREADS_NUMBER)]
[t.join() for t in threads]

