from bisect import bisect, bisect_left, insort

lst = [1,2,3,4,5,6,9]

pos = bisect(lst, 2)

pos2 = bisect(lst, 8)

# Insert in order with insort():

lst2 = []
for i in [4,3,5,1,2]:
    insort(lst2, i)
    
print(lst2)

