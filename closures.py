## Closures & nonlocal:

# First take on averager:
def make_averager_1():
    series = []
    
    def averager(new_val):
        series.append(new_val)
        total = sum(series)
        return total/len(series)
    
    return averager
    
    
avg = make_averager_1()
print(avg(10))
print(avg(11))
print(avg(12))

# series is a closure in averager:
print('vars: ', avg.__code__.co_varnames)
print('avg\'s closure: ', avg.__closure__[0].cell_contents)


# Second take on averager: [ERRONEOUS IF LACKS nonlocal declaration !]
def make_avg():
    total = 0
    count = 0
    
    def avg(new_val):
        nonlocal count, total # needed here, because count += 1 will make count local otherwise
        # that will lead to count being local and not captured in the closure of avg().
        count += 1
        total += new_val
        return total / count
    
    return avg


avg = make_avg()
print(avg(10))