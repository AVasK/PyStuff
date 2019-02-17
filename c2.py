class vector:
    def __init__(self, lst):
        self.storage = list(lst)
        self.ptr = 0
    def __add__(self, lst):
        return vector([x + y for x, y in zip(self.storage, list(lst))])
    
    def __radd__(self, lst):
        return self.__add__(lst)
    
    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return ':'.join(map(str, self.storage))
    
    def __iter__(self):
        for i in self.storage:
            yield i
            
