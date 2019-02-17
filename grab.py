a, b, c = (1,2,3)
head, *tail = [1,2,3,4]
print(head, '.', tail)
# 1.[2,3,4]

# This means we can do pattern-matching in prolog/haskell style in Python.

def pmatchedReverse(arr, acc):
    head, *tail = arr
    
    if tail:
        return pmatchedReverse(tail, [head] + acc)
    else:
        return [head] + acc