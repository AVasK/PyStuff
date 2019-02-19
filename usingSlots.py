## Using __slots__ class attribute when
## in a situation with a few attributes, 
## many instances and a memory shortage.

class almostPOD():
    
    __slots__ = ('caption', 'number')
    
    def __init__(self, caption, number):
        self.caption = str(caption)
        self.number  = int(number)
        
    def __str__(self):
        return self.caption + str(self.number)
    
    def __repr__(self):
        return str(self)