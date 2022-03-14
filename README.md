# 1. Analysis

There are few synchronization problems. 

- data writing into shared drive. 
- monitor update
- data validation

# 2. Primitives mapping

For each problem we mapped different synchronization methods.

- data writing will be handled by LightSwitch
- monitor update by Turnstile
- data validation by Barrier


