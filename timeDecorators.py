# Timing Decorators:

import time
import functools

def timeit(f):
    @functools.wraps(f)
    def clocks(*args, **kwargs):
        t = time.perf_counter()
        result = f(*args, **kwargs)
        t = time.perf_counter() - t
        
        args = ', '.join(repr(arg) for arg in args) + (', ' if kwargs else '')  +\
               ', '.join('%s = %r' % (key, val) for key, val in kwargs.items())
        print(f"<timeit {f.__name__}({args})> {t:.3f} sec.")
        
        return result
    return clocks


def avgTime(N_iters = 3):
    def avgTimeDeco(f):
        @functools.wraps(f)
        def timer(*args, **kwargs):
            T = 0
            for n in range(N_iters):
                t = time.perf_counter()
                res = f(*args, **kwargs)
                t = time.perf_counter() - t
                T += t
            
            T /= N_iters
            
            args = ', '.join(repr(arg) for arg in args) + (', ' if kwargs else '')  +\
                   ', '.join('%s = %r' % (key, val) for key, val in kwargs.items())
            print(f"<avgTime {f.__name__}({args}) @ {N_iters} runs: {T:.3f} s.>")

            return res
        return timer
    return avgTimeDeco



""" Example of Usage: """

if __name__ == "__main__":
    
    @timeit
    def sleep(s):
        time.sleep(s)
    
    #sleep(1)
    
    @timeit
    @avgTime(10) # will impact @timeit readings.
    def f(a, b, *, c = 5):
        a = (a * b ** (200*c))

    f(124, 200, c = 344)