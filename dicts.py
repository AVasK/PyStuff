## Dict:

# Inheritance:
#
# [Container]<- 
#              \
# [Iterable]<- - [Mapping] <- [MutableMapping]
#              /
# [Sized]   <-
#

# Many ways to create a dict
a = dict(one = 1, two = 2, three = 3)
b = {'one' : 1, 'two' : 2, 'three' : 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('one', 1), ('two', 2), ('three', 3)])

print(a == b == c == d)

# Dict comprehensions (since v2.7)
DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'US'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]

country_code = {country : code for code, country in DIAL_CODES} # < Dict comprehension.

print(country_code)

print({code : country for country, code in country_code.items() if code < 10})


# SETDEFAULT:

d = {}

for key in ['zero', 'one', 'two', 'three', 'four', 'five']:
    d.setdefault(key, 0)
    
print(d)


# using defaultdict & overloading __missing__():

from collections import defaultdict

dd = defaultdict(list) # uses list() constructor as a default_factory method.
dd['q'].append('q') # even though we don't have 'q' key, we can address it
# instead of raising an exception, defaultdict will use default_factory constructor
# to create a new value and will then initialize a new key-value pair.

dd['qq'].append('qq')
print(dd)

ddi = defaultdict(lambda : 0)
print(ddi[100])
print(ddi.items())

# Second approach: overload __missing__ in subclass:

class strDict (dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
    
    def get(self, key, default = None):
        try:
            return self[key]
        except KeyError:
            return default
        
    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()
    
    
s = strDict({"0" : 0, "1" : 1})
print(s['1'])
#s[1] = 2 ## this one would not work. overload __setitem__?
print(s[1])


import collections
# This one works both for set and get.
class StrDict2 (collections.UserDict):
    
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError
        return self[str(key)]
    
    def __contains__(self, key):
        return str(key) in self.data
    
    def __setitem__(self, key, item):
        self.data[str(key)] = item
        
