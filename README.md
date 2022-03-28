# PPDS

## The rollercoster

This time i took time to implement the rollercoaster synchronisation problem.

Program is functioning by first loading cart with passengers of constant size.
After that cart is ran and on after that all passengers unboard. 
Only 1 cart can be loaded and unloaded at the same time.

Shared data contains:
 - loading_area : Semaphore[] for each cart
 - unloading_area : Semaphore[] for each cart
 - board_queue : boarding q for passengers
 - unboard_queue : unboarding q for passengers
 - boarded : barrier for when cart is loaded
 - unboarded : barrier for when cart is unloaded



