## a simple example of Vector2D class

from array import array
import math

class Vector2D:
    typecode = 'd'
    
    __slots__ = ('__x', '__y')
    
    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)
    
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
        
    def __iter__(self):
        return (i for i in (self.x, self.y))
    
    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)
    
    def __str__(self):
        return str(tuple(self))
    
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))
    
    def __eq__(self, other):
        return tuple(self) == tuple(other)
    
    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    def __bool__(self):
        if self.x == 0 and self.y == 0:
            return False
        return True
    
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)
    
    @staticmethod
    def static_f(a):
        print(a)
        
    def angle(self):
        return math.atan2(self.y, self.x)
        
   
    # Adding custom formatting:
    def __format__(self, fmt_spec = ''):
        print(fmt_spec) # We get the formatting string (the one after :), hence
        # we can create our own formatting conventions!
        
        if fmt_spec.startswith('i'):
            fmt_spec = 'n'
            outer_fmt = '({}, {})'
            coords = (int(c) for c in self)
        elif fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (self.__abs__(), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
            
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)
    
    
    # Make it hashable:
    def __hash__(self):
        return hash(self.x) ^ hash(self.y)
    
    
    