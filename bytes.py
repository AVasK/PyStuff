# operating with bytes & memoryviews:

# ex.1:
sb = bytes('≈•••≈', encoding = 'utf_8')

"""
>>> ba[0] = 0
>>> ba[1] = 0
>>> ba[2] = 9
>>> ba
bytearray(b'\x00\x00\t\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x89\x88')
>>> ba.decode('utf_8')
'\x00\x00\t•••≈'
>>> b = bytearray([])
>>> b
bytearray(b'')
>>> b.append(1)
>>> b
bytearray(b'\x01')
>>> b = bytearray([0,1,1,0])
>>> b
bytearray(b'\x00\x01\x01\x00')
>>> b[:1]
bytearray(b'\x00')
>>> for i in range(len(b)):
...     b[i] += 1
... 
>>> b
bytearray(b'\x01\x02\x02\x01')
>>> size(b)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'size' is not defined
>>> sizeo(b)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sizeo' is not defined
>>> sizeof(b)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sizeof' is not defined
>>> b[0] = 277
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: byte must be in range(0, 256)
>>> b[0] = 255
>>> b
bytearray(b'\xff\x02\x02\x01')
>>> b[0] = 256
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: byte must be in range(0, 256)
>>> b
bytearray(b'\xff\x02\x02\x01')
>>> import arrray
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'arrray'
>>> import array.array
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'array.array'; 'array' is not a package
>>> import array
>>> b = bytearray(array.array('b', [1,2,3,4,5]))
>>> b
bytearray(b'\x01\x02\x03\x04\x05')
>>> b = bytearray(array.array('h', [1,2,3,4,5]))
>>> b
bytearray(b'\x01\x00\x02\x00\x03\x00\x04\x00\x05\x00')
>>> b = bytearray(array.array('b', [1,2,3,4,5]))
>>> b
bytearray(b'\x01\x02\x03\x04\x05')
>>> a = array.array('b', [0,] * 10)
>>> a
array('b', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
>>> a[1] = 256
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
OverflowError: signed char is greater than maximum
>>> a[1] = 255
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
OverflowError: signed char is greater than maximum
>>> a[1] = 127
>>> a[1] = 128
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
OverflowError: signed char is greater than maximum
>>> a
array('b', [0, 127, 0, 0, 0, 0, 0, 0, 0, 0])
>>> a = array.array('ub', [0,] * 10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: array() argument 1 must be a unicode character, not str
>>> a = array.array('u', [0,] * 10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: array item must be unicode character
>>> a = array.array('c', [0,] * 10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: bad typecode (must be b, B, u, h, H, i, I, l, L, q, Q, f or d)
>>> typecode('h'
... )
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'typecode' is not defined
>>> a = array.array('u', [0,] * 10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: array item must be unicode character
>>> a = array.array('B', [0,] * 10)
>>> a[1] = 128
>>> a[1] = 255
>>> a[1] = 256
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
OverflowError: unsigned byte integer is greater than maximum
>>> s
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 's' is not defined
>>> a
array('B', [0, 255, 0, 0, 0, 0, 0, 0, 0, 0])
>>> memoryview(a)
<memory at 0x10ea53c48>
>>> am = memoryview(a)
>>> am
<memory at 0x10ea53dc8>
>>> am[1]
255
>>> am[0]
0
>>> am[:]
<memory at 0x10ea53c48>
>>> am[:-1]
<memory at 0x10ea53e88>
>>> am[1:-1]
<memory at 0x10ea53c48>
>>> am[2] = 2
>>> a
array('B', [0, 255, 2, 0, 0, 0, 0, 0, 0, 0])
>>> am[3] = 4
>>> a
array('B', [0, 255, 2, 4, 0, 0, 0, 0, 0, 0])
>>> for i in am:
...     print(i)
... 
0
255
2
4
0
0
0
0
0
0
>>> for i in range(len(am)):
...     i += 1
... 
>>> a
array('B', [0, 255, 2, 4, 0, 0, 0, 0, 0, 0])
>>> for i in range(len(am)):
...     am[i] += 1
... a
  File "<stdin>", line 3
    a
    ^
SyntaxError: invalid syntax
>>> for i in range(len(am)):
...     am[i] += 1
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ValueError: memoryview: invalid value for format 'B'
>>> a
array('B', [1, 255, 2, 4, 0, 0, 0, 0, 0, 0])
>>>     am[i] -= 10
  File "<stdin>", line 1
    am[i] -= 10
    ^
IndentationError: unexpected indent
>>> for i in range(len(am)):
...     am[i] -= 10
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ValueError: memoryview: invalid value for format 'B'
>>> a
array('B', [1, 255, 2, 4, 0, 0, 0, 0, 0, 0])
>>> am[1] = 0
>>> for i in range(len(am)):
...     am[i] += 10
... 
>>> a
array('B', [11, 10, 12, 14, 10, 10, 10, 10, 10, 10])
>>> a[0] & a[1]
10
>>> am[0] & am[4]
10
>>> am[0] & am[4]
10
>>> am[0] & am[3]
10
>>> am[0]
11
>>> bin(am[0])
'0b1011'
>>> bin(am[3])
'0b1110'
>>> bin(am[0] & am[3])
'0b1010'
>>> am[0] | am[3]
15
>>> 
"""


import struct
fmt = '<3s3sHH'
# 
# <  - little-endian
# 3s - 3-byte seq 
# H  - sHort (16-bit) int.

