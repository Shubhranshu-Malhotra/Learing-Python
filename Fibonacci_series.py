from time import time
# def fibonacci(num): 
#     fib = []
#     for i in range(0,num+1):
#         if(i != 0 and i != 1):
#             fib.append(fib[i-1]+fib[i-2])
#         else:
#             fib.append(i)
#     return fib
def fibonacci(num): 
    a = 0
    b = 1
    fib =[]
    for _ in range(0,num+1):
        fib.append(a)
        temp = a
        a = b
        b = temp + b
    return fib

t1 = time()
print(fibonacci(200))
t2 = time()

def fibonacci_2(num): 
    a = 0
    b = 1
    temp = 0
    for _ in range(0,num+1):      
        yield a
        temp = a
        a = b
        b = temp + b
           
 
t3 = time()
for i in fibonacci_2(200):
    print(i)
t4 = time()
print(f'total time taken with lists {t2 - t1} seconds')

print(f'total time taken with yield {t4 - t3} seconds')