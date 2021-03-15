from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
def capitalize_names(name):
    return name.upper()
print(list(map(capitalize_names,my_pets)))

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]
print(list(zip(my_strings, sorted(my_numbers))))


#3 Filter the scores that pass over 50%
def get_50_above(score):
    return score>50

scores = [73, 20, 65, 19, 76, 100, 88]

print(list(filter(get_50_above, scores)))

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

def sum_all_lists(prev, num):
    return prev+num

print(reduce(sum_all_lists, scores, reduce(sum_all_lists, my_numbers, 0)))
# OR
print(reduce(sum_all_lists, my_numbers + scores))