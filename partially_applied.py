from functools import partial, wraps

def partially_applied(_f, *args):
    @wraps(_f)
    def partial_maker(*args):
        if len(args) == _f.__code__.co_argcount:
            return _f(*args)
        else:
            return partial(_f, *args)
    return partial_maker

if __name__ == "__main__":
    # testing time:
    
    @partially_applied
    def make(a, b, c):
        return (a, b, c)
    

    f = make
    for _ in range(3):
        print(f)
        f = f(0)
      
    print(f)
     
    o = make(1,2)
    print(o)
    o = o(3)
    print(o)