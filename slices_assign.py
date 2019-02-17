## Slice assignment (some cool things going on here)

l = list(range(10))
print(l)
#>>> l = [0,1,2,3,4,5,6,7,8,9]

l[0:3] = [-1, -2]
print(l)
#>>> l = [-1, -2, 3, 4, 5, 6, 7, 8, 9]

l[2:3] = [10,20,30]
print(l)
#>>> l = [-1, -2, 10, 20, 30, 4, 5, 6, 7, 8, 9]