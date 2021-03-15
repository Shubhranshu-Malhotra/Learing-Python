# # 1) To handle any kind of error
# while True:
#     try:
#         age = int(input('What is your age?'))
#         print(age)
#         # break
#     except:
#         print('Please enter a valid age!')
#     else:
#         print('thank you!')
#         break

# # 2) To handle any kind of error
# while True:
#     try:
#         age = int(input('What is your age?'))
#         print(10/age)
#         # break
#     except ValueError:
#         print('Please enter a number!')
#     except ZeroDivisionError:
#         print('please enter an age higher than zero!')
#     else:
#         print('thank you!')
#         break

# # 3) Using Error handling inside function, storing and displaying error message
# # and handling multiple types of errors within a single except

# def sum(num1, num2):
#     try:
#         return num1/num2
#     except (TypeError, ZeroDivisionError) as err:
#         print(f'Oops!! {err}')

# print(sum(1,0))

# # 4) Using the `finally` block
# while True:
#     try:
#         age = int(input('What is your age?'))
#         print(10/age)
#         # break
#     except ValueError:
#         print('Please enter a number!')
#     except ZeroDivisionError:
#         print('please enter an age higher than zero!')
#     else:
#         print('thank you!')
#         break
#     finally: # always runs whether exception occur or not
#         print('ok, I am finally done!')


# 4) Raising our own error  ## Try by inputing a number in age
while True:
    try:
        age = int(input('What is your age?'))
        print(10/age)
        raise ValueError('hey! Cut it out.')
    # except ValueError:
    #     print('Please enter a number!')
    except ZeroDivisionError:
        print('please enter an age higher than zero!')
    else:
        print('thank you!')
        break
    finally: # always runs whether exception occur or not
        print('ok, I am finally done!')

