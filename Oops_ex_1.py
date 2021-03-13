# OOPS EXERCISE 1

# Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 1) Instantiate the cat object with 3 cats.

cat1 = Cat('tin', 1)
cat2 = Cat('pin', 0.5)
cat3 = Cat('lin', 2)



# WAY 1


# 2) Create a function that finds the oldest cat

def get_oldest(cats):
    oldest_cat = ''
    highest_age = -1
    for cat in cats:
        if cat.age > highest_age:
            highest_age = cat.age
            oldest_cat = cat.name
    return oldest_cat, highest_age


# 3) Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

oldest_cat, highest_age = get_oldest([cat1, cat2, cat3])
print(f"The oldest cat is {oldest_cat} and she is {highest_age} years old.")



# WAY 2



# 2) Create a function that finds the oldest cat

def get_oldest_2(*args):
    # return max(args) # if taking just the ages as input
    return max( e.age for e in args)


# 3) Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

highest_age = get_oldest_2(cat1, cat2, cat3)
print(f"The oldest cat is {highest_age} years old.")