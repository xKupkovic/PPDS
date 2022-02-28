from fei.ppds import Mutex,print,Semaphore,Thread

def get_next_fibonacci(i):
    return nums[i-2]+nums[i-1]
    pass

def fibonacci_cycle(thread_id):
    global t
    nums.append(get_next_fibonacci(thread_id+2))
    pass
    
THREADS_NUMBER = 5

t = Semaphore(0)

calculated = 0

nums = []

nums.append(0)
nums.append(1)

threads = [ Thread(fibonacci_cycle,i) for i in range(THREADS_NUMBER)]
[t.join() for t in threads]

print(nums)

