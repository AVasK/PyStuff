from functools import singledispatch

import numbers
from collections import abc


# A simple function that behaves differently for different types,
# and thus would benefit from overloading:

@singledispatch
def react(obj):
    print('I recieved an inudentified obj!')
    
    
@react.register(numbers.Integral)
def _(n):
    print('I recieved a number... It\'s {}'.format(n))

@react.register(str)
def _(s):
    print('I see... You really mean that ' + s)

@react.register(tuple)
@react.register(abc.MutableSequence)
def _(seq):
    print('Detecting multiple packets... Server OFFLINE. Bye.')

    
    
"""

Console -i Output:

>>> react(2)
I recieved a number... It's 2
>>> react('sss')
I see... You really mean that sss
>>> react((1,2,3))
Detecting multiple packets... Server OFFLINE. Bye.
>>> react({1:'x'})
I recieved an inudentified obj!
>>> react(2.2)
I recieved an inudentified obj!
>>> 

"""