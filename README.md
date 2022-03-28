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

### Testing

By printing out functions of when is cart loading and unloading I observed that unloading is possible only when all passengers
unboarded from previouse and loading is possible only after cart has started running.
Different people can board and unboard at the same time but only 5 for each at the time.

