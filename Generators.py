# Making your own Generator

def generator_func(num):
    for i in range(num):
        yield i

for i in generator_func(10):
    print(i*2)

g = generator_func(10)
print(g)
print(next(g))
print(next(g))
print(next(g))

