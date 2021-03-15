from functools import reduce
my_list = [1, 2, 3]
print(list(map(lambda item:item*2, my_list))) # SIGNATURE: lambda param: action(param)
print(list(filter(lambda item: item>=2, my_list)))
print(reduce(lambda acc, item: acc+item, my_list))

print(list(map(lambda item: item**2, my_list)))

# List sorting by second element of tuple
a = [(0,2), (4,3), (9,9), (10, -1)]
a.sort(key = lambda x: x[1])
print(a)