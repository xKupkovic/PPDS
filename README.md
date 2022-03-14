# 1. Analysis

There are few synchronization problems. 

- data writing into shared drive. 
- monitor update
- data validation

# 2. Primitives mapping

For each problem we mapped different synchronization methods.

- data writing will be handled by LightSwitch
- monitor update by Turnstile
- data validation by Event

# 3. PseudoCode

``` python

all_sensor_threads = start_sensor_threads()
all_monitor_threads = start_monitor_threads()

initialize_shared_data()

------------------------------------
for sensor in all_sensor_threads:
    while True:
        sensor_wait()
        sensor_write_data()
        sensor_signal()
        valid_data_signal()
        
for monitor in all_monitor_threads:
    valid_data_wait()
    while True: 
        monitor_wait()
        monitor_read_data()
        monitor_signal()      
   
```     