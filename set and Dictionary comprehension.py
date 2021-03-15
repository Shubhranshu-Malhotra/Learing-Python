# Dictionary Comprehension
simple_dict = {
    'a':1,
    'b':2,
    'c':3
}
my_dict = {key:value**2 for key, value in simple_dict.items() if value%2 != 0}
new_list = [1,2,3]
my_dict_2 = {num:num*2 for num in new_list}
print(my_dict)
print(my_dict_2)
# Set comprehension is same as list comprehension

#Using simple function

my_set = set()
for char in 'hello':
    my_set.add(char)
print(my_set)

# Using a set comprehension

# Signature: {param for param in iterable}

my_set_comprehension = {char for char in 'hello'}
print(my_set_comprehension)

my_set_comprehension_2 = {num**2 for num in range(1,10)}
print(my_set_comprehension_2)

my_set_comprehension_3 = {num**2 for num in range(0,10) if num % 2 == 0}
print(my_set_comprehension_3)

