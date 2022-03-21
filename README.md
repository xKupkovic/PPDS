# PPDS

## Dining Savages

Program simulates modified sync problem of dinning savages.

When savage finds out that pot is empty he wakes all the cooks. They all start cooking concurently 
and when the meal is cooked last cook will tell it to the waiting savage.

Base of program is taken from https://uim.fei.stuba.sk/i-ppds/5-cvicenie-problem-fajciarov-problem-divochov-🚬/


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

# 4. Program description

- class ```Shared```:
  - Shared data for threads
- class ```SimpleBarrier```:
  - Simple barrier used to wait for all cooks to finish
- function ```savage()```
  - Function simulate savages eating from pot, it waits for it to get filled by cooks when empty
- function ```cook()```
  - Waits until pot is empty, after that cooks servings until maximum is reached, after it signals savages
- function ```fill_pot()```
  - Sets servings in shared data and signals full pot
  - Called from SimpleBarrier after overflow