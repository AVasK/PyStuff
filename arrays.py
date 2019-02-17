# Arrays:

from array import array
from random import random

f_arr = array('d', (random() for i in range(100))) # 100 floats (d = double)

i_arr = array('i', (int(random()*10)  for i in range(10))) # 10 ints

with open('floats.bin', 'wb') as file:
    f_arr.tofile(file) # writes to binary file
    
f_arr_2 = array('d')
with open('floats.bin', 'rb') as file:
    f_arr_2.fromfile(file, 100) # reads from binary file


i_arr += array('i', [7,7,7]) # we can still operate on arrays as if those are single-type lists.

print(i_arr)

i2_arr = array('i', (i for i in range(10)))

print(i2_arr + i_arr)