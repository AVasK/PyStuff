### Function registry decorator:

registry = []

def mark(func):
    registry.append(func)
    return func


if __name__ == "__main__":
    
    # Testing:
    
    @mark
    def func1(a, b):
        return a + b
    
    @mark
    def func2(a, b):
        return a * b
    
    print(registry)
    
    for i in range(len(registry), -1, -1):
        del(registry[i])
        
    print(func1(2,3))