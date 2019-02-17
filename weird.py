### __iadd__ for mutables & immutables
# ! behaves differently

# for list += *= and others work in-place
l = [1,2,3]
print(id(l))
l *= 2
print(id(l))

# for immutables they don't, they get translated to 
### t = t <op> 2

t = (1,2,3)
print(id(t))
t *= 2
print(id(t))


### NOW, Magic!

w = (1, 2, [3, 4])
w[2] += [4, 5]

# What's gonna happen?
# : it's gonna chash, bc u're changing an immutable.
# : yet, inside the w[2] gonna be [3,4,4,5]!!!
