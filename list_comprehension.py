#Using simple function

my_list = []
for char in 'hello':
    my_list.append(char)
print(my_list)

# Using a list comprehension

# Signature: [param for param in iterable]

my_list_comprehension = [char for char in 'hello']
print(my_list_comprehension)

my_list_comprehension_2 = [num**2 for num in range(1,10)]
print(my_list_comprehension_2)

my_list_comprehension_3 = [num**2 for num in range(0,10) if num % 2 == 0]
print(my_list_comprehension_3)