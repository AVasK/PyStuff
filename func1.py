"""

Playing with functions.

"""

"""
Each function can have:

__annotations__ : dict of annotations (Ex. {'a' : <class 'int'>})
__call__ : implementation of the () operator - callable object protocol
__closure__ : tuple containing the closure of function
__code__ : byte-code <class 'code'> of func body
__defaults__ : tuple of default args [in hard-to-use form]
__get__ : implements read-only descriptor protocol. 
__globals__ : dictionary of globals in the module where the aforementioned function belongs to.
__kwdefaults__ : dict of defaults for keyword-only args.
__name__ : name.
__qualname__ : qualified name (modules included).

"""

# trivial function declaration
def f(a, b):
    return a + b

# with default values:
def f_def(a = 1, b = 2):
    return a + b

## EASY ?
## LVL UP !

# functions with *args:
def f_args(*args):
    if len(args) == 2:
        a, b = args
        return a + b
    
def f_argskwargs(*args, **kwargs):
    if len(args) == 2:
        return sum(map(int, args))
    
    else:
        print(args, kwargs)
        
## PRINT-OUT:_____________________
## f_argskwargs(1,2,3, a=2, c = 3)
## >>>  (1, 2, 3) {'a': 2, 'c': 3}
## _______________________________


# still boring?
# continuing...

# keyword-only parameters:
def f_kwonly(a, *, b):
    return a + b

# same, but now it doesn't have ANY positional args.
def f_kwonly2(*, a, b):
    return a + b

# Inspection:
from inspect import signature

def f(a = 1, s = "str"):
    return f"{a} {s}"

def f2(a : int, s : str):
    return a

def info(func):
    sign = signature(func)
    print(f"{func.__name__}{sign}")
    

## Binding parameters to func values:
s = signature(f_kwonly2)
args = s.bind(a = 1, b = 2)
for name, value in args.arguments.items():
    print(f"{name} -> {value}")
#
# a -> 1
# b -> 2
    


