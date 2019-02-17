## Generator expressions come in 2 flavours:

lst = [x for x in range(10)] # keeps all the array in memory
# returns a list

gen = (x for x in range(10)) # works as iterable, real-time computation
# returns a generator
