from fei.ppds import Mutex,print,Semaphore,Thread

def get_next_fibonacci(i):
    return nums[i-2]+nums[i-1]
    pass

def fibonacci_cycle(thread_id):
    global t,count
    while(thread_id != count):
        t.wait()
        t.signal()
        pass
    t.signal()
    count+=1
    nums.append(get_next_fibonacci(thread_id+2))
    pass
    
THREADS_NUMBER = 20

t = Semaphore(0)

count = 0

nums = []

nums.append(0)
nums.append(1)

threads = [ Thread(fibonacci_cycle,i) for i in range(THREADS_NUMBER)]
[t.join() for t in threads]

print(nums)
