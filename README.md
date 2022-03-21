# PPDS

# 1. Analysis

- Program is composed of 2 task, where on each can be assigned multiple workers.
- Each task is requires different workers.
- Tasks can not be executed simultaneously 
- Program needs to wait for each worker to finish on each task
- Last worker should signalize new task to begin

# 2. Pseudocode

```python
cooks: Thread(cook)
savages: Thread(savage)
max_servings: number of pot servings
____________________________________________
while True:
    while True:
        for thread_cook in cooks:
            meal_number = cook.cook_meal()
            if meal_number == max_servings:
                wait_threads()
                break
    while True:
        for thread_savage in savages:
            meal_number = savage.eat()
            if meal_number == 0:
                wait_threads()
                break            

```

# 3. Check 

Print function is called:
- For each cook when start cooking
- For last cook to finish cooking
- For each savage start eating

Print calls in program are proof that it works.