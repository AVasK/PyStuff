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
    
    ## <!> ACHTUNG: When using __slots__, instances of the class
    #  will not be allowed to have any other attributes but those
    #  specified in __slots__. That's kinda a drawback, but it's 
    #  solveable. [see NOTE]
    
    ## <!> NOTE: you can add '__dict__' to __slots__ iterable,
    #  so it will support both methods, but you risk cancelling the 
    #  traits of __slots__ then. Always stay vigilant.