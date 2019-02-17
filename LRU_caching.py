from timeDecorators import timeit
import functools
## Computationally stupid Fibonacci is used for illustrative purposes
    
#@functools.lru_cache() # LeastRecentlyUsed caching (memoization).
#@timeit
def stupid_fib(n):
    if n < 2:
        return n
    else:
        return stupid_fib(n-2) + stupid_fib(n-1)

import time

t = time.perf_counter()
print(stupid_fib(20)) # really dumb-ass implementation
t = time.perf_counter() - t
print('%.4f' % t)

stupid_fib = functools.lru_cache()(stupid_fib)

t = time.perf_counter()
print(stupid_fib(20)) # not so stupid with lru_cache!
t = time.perf_counter() - t
print('%.4f' % t)

# The difference is huge - we get a totally 
# viable algorithm from what is considered the worst func ever...

""" !!! LRU_cache can have parameters: """
#   @functools.LRU_cache(maxsize = ..., typed = False)
#                        ^              ^
#           how many calls remembered   |
#                                       |
#                  holds the invocations with different types of args separately
#                [e.g.:  1.0 and 1 as an argument are by default considered equal]


