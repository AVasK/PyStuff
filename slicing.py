# Slicing:

import numbers

class MySeq:
    def __getitem__(self, index):
        print(index)
        return index
    
s = MySeq()
s[1]    # -> 1
s[1:4]  # -> slice(1, 4, None)
s[1:4:2]# -> slice(1, 4, 2)
s[1:4:2, 9] # -> (slice(1, 4, 2), 9)
s[1:4:2, 7:9] # -> (slice(1, 4, 2), slice(7, 9, None))


# Slice methods:
print(dir(slice))

## Slice.indices(len) -> (start, stop, stride)

print(slice(None, 6, 3).indices(5)) # -> (0, 5, 3)


## Implementing a slice-aware getitem:

class Sliceable(): # Just a trivial example of Sliceable class...
    def __init__(self, name, value):
        self.name  = list(name)
        self.value = list(value)
    
    # Supporting functions for ease of demonstration
    def __str__(self):
        return str(list(zip(self.name, self.value)))
    
    def __repr__(self):
        return str(self)
    
    # The main part of discussion is here:
    def __getitem__(self, idx):
        cls = type(self)
        if isinstance(idx, slice):
            return cls(self.name[idx], self.value[idx])
        elif isinstance(idx, numbers.Integral):
            return self.name[idx], self.value[idx]
        else:
            msg = '{cls.__name__} indices must be integers'.format(cls = cls)
            raise TypeError(msg)
        
            
    
    