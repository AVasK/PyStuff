import time
for n in (100000, 200000, 300000, 400000):
    data = ('x'*n).encode('ASCII')
    start = time.time()
    b = data
    while b:
        b = b[1:]
    print('bytes', n, time.time()-start)

for n in (100000, 200000, 300000, 400000):
    data = ('x'*n).encode('ASCII')
    start = time.time()
    b = memoryview(data)
    while b:
        b = b[1:]
    print('memoryview', n, time.time()-start)