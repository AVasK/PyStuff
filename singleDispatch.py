## SingleDispatch: [@ py v. > 3.4]

"""

Single Dispatch is somewhere near function overloading with respect to only one (fisrt) parameter - 
    hence the name *single* dispatch. 
    
Example to how single dispatch works follows:
[book reference: fluent python]

"""


##
## Example 1:
##

from functools import singledispatch
# imports needed datatypes' ABCs:
from collections import abc
import numbers
# specific to example
import html

@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

@htmlize.register(str) #<!> each overloading is decorated with @<base_func>.register(type) 
def _(text): #<!> _ denotes that we don't care about function's name.
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)

@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)

@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'



