import operator

metro_data = [
    ('Tokyo', 'JP', 36.933),
    ('Delhi NCR', 'IN', 21.935),
    ('Mexico City', 'MX', 20.142),
]

for city in sorted(metro_data, key = operator.itemgetter(2)):
    print(city)
    
    
cc_name = operator.itemgetter(1, 0) # itemgetter will construct tuples if passed more than 1 arg.
for city in metro_data:
    print(cc_name(city))
    
    