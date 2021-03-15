def my_decorator(func):
    def wrap_func():
        print('*********')
        func()
        print('*********')
    return wrap_func   

@my_decorator
def hello():
    print('hellooo!!!')

hello()

# Same functionality as the below code 

# hello2 = my_decorator(hello)
# hello2()
print()

# passing any number of arguments to decorators

def my_decorator_2(func):
    def wrap_func(*args, **kwargs):
        print('*********')
        func(*args, **kwargs)
        print('*********')
    return wrap_func   

@my_decorator_2
def hello2(greetings, emoji = ':)'):
    print(greetings, emoji)

hello2('hi')