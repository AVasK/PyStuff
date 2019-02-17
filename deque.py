## Deques:
from collections import deque

dq = deque([], maxlen = 4) # setting maxlen leads to bounded deque.
                      #^ optional argument

# run the -i (interactive) mode and play with it

# commands are:
#> append(elem)
#> appendleft(elem)
#> extend([elems])
#> extendleft([elems]) where [elems] would be reversed on insertion.
#> rotate(n)

### APPEND & POPLEFT are ATOMIC => SAFE TO USE as STACK IN MULTI-THREADED APPS.
