### If you're willing to partially apply some function
### if you hanker to do some functional programming
### ...
from functools import partial, wraps
### Henceforth you can do so

### time to Roll Out Some Haskell examples?
from operator import mul
mul_2 = partial(mul, 2)
print(list(map(mul_2, [1,2,3,4,5])))

list_square = partial(map, lambda x : x * x)
print(list(list_square([1,2,3])))

### And if you wish to do it in even more functional way...
### ...
### Well, you can.
### [BEWARE, IT LOOKS CLUMSY]

def _func(a, b, c):
    return a + b + c

def func(*args):
    if len(args) == _func.__code__.co_argcount:
        return _func(*args)
    else:
        return partial(_func, *args)
    
    
print(func(1,2,3))
print(func(1,2))

f = func(2,3)
print(f(4))


def mk_partial(_f, *args):
    @wraps(_f)
    def partial_maker(*args):
        if len(args) == _f.__code__.co_argcount:
            return _f(*args)
        else:
            return partial(_f, *args)
    return partial_maker

@mk_partial
def f2(a, b):
    print("in f: ", a, b)
    return a + 2*b

@mk_partial
def print_greeting(s1, s2):
    print(s1, s2)

