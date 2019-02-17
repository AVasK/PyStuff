# playing with memoryview:
import array

arr = array.array('h', (x for x in range(10)))

view = memoryview(arr)
viewslice = view[::2] # now we can work with a slice as if it is an array

