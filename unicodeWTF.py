# To work with unicode, we need to normalize it:

c1 = 'café' 
c2 = 'cafe\u0301'

print(len(c1), len(c2))
# > 4, 5
# so, they are different
# but they look similar.

print(c1 == c2) # False!

from unicodedata import normalize
print(normalize('NFC', c1) == normalize('NFC', c2)) # Now it's True. 

mu1, mu2 = '\u00B5', '\u03BC'
print('\u00B5', '\u03BC') # both are greek µ's. They're NOT equal.
print(mu1 == mu2) # NOPE.
print(normalize('NFC', mu1) == normalize('NFC', mu2)) # NOT YET. Even normalized with NFC.
print(normalize('NFKC', mu1) == normalize('NFKC', mu2)) # Now they ARE EQUAL. (WTF, unicode?)

# Now, it is SO tempting to use only NFKC form, right? 

# But if you think that the trouble is over now
# you are mistaken, LOL.

c = '4º'
print(normalize('NFKC', c)) # >> 4o. 
# more indicative examples: '4^2 -> 42' and \u{half_sign} -> 1/2


# BTW, you can freely use utf-8 chars in Python code. For better or worse)
ß = 1
print(ß)

s1 = 'ß'
print(s1.casefold()) # like str.lower() but supports Unicode.


import unicodedata
# A way to delete all diacritics:
def delete_marks(utf_str):
    norm_form = unicodedata.normalize('NFD', utf_str)
    clean = ''.join(filter(lambda c: not unicodedata.combining(c), norm_form))
    
    return unicodedata.normalize('NFC', clean)