from fei.ppds import Mutex,print,Event,Thread

def get_next_fibonacci(i):
    return nums[i-2]+nums[i-1]
    pass

def fibonacci_cycle(thread_id):
    global t,count
    while(thread_id != count):
        t.wait()
        t.signal()
        pass
    nums.append(get_next_fibonacci(thread_id+2))
    count+=1
    t.signal()
    pass
    
THREADS_NUMBER = 5

t = Event()

count = 0

nums = []

nums.append(0)
nums.append(1)

threads = [ Thread(fibonacci_cycle,i) for i in range(THREADS_NUMBER)]
[t.join() for t in threads]

print(nums)

