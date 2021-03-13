class Toy():
    def __init__ (self, color, age):
        self.color = color
        self.age = age
        self.mydict = {
            'name' : 'Yoyo',
            'has_pets' : False
        }

    def __str__(self):
        return f'{self.color}'
    
    def __del__(self):
        print('deleted!')

    def __call__(self):
        return 'Yess!!!'

    def __getitem__(self, i):
        return self.mydict[i]

action_figure = Toy('red', 0)

# Dunder method can be called using multiple ways.Eg for str: x.__str__() OR str(x). Different dunder methods can be called in different ways
print(action_figure.__str__()) 
print(str(action_figure)) #  Dunder method overridden for the Toy() class
print(str('action_figure')) # Overriding dinder method above doen't affects its functioning on other objects

print(str (action_figure))
print(action_figure()) # can be called like a function because we have __call__ in our class

print(action_figure['name']) # able to use [] square brackets because of the __getitem__ dunder