import sys
import random



# Custom Exceptions
class HugeRangeError(Exception):
    """Raised when range exceeds 500"""
    pass

class OutOfRangeError(Exception):
    """Raised when the input value is out of the specified range"""
    pass


# Function for testing
def game():
    pass


count = 0
start = 0
stop = 10

# Get the range input from user
# while(True): # cant use while loop to take input again since taking as argv input 
try:
    # if(sys.argv[1]):
    start = int(sys.argv[1])
    # if(sys.argv[2]):
    stop = int(sys.argv[2])
    if stop - start > 500:
        raise HugeRangeError
except ValueError: 
    print('please enter an integer')
    exit()
except HugeRangeError:
    print('the maximum range has been restricted to 500!')
    exit()
# else:
#     break


# GAME INSTRUCTIONS
print()
print(' Guide: This game starts by you entering a range of numbers as command line argiments.')
print('The system then generates a random number in that range and your job is to guess it.')
print( 'Your tries are limited to 10')
print('Remember if you find the game hard you can always take a hint!!')

print('A new random number is generated each time you guess it wrong.')
print()


# Main Game

# Loop to shut down game if max trials exceed
while(True):

    # generating a random guess between {start} and {stop}
    random_num = random.randint(start, stop)
    # print('generated integer: ', random_num) # for testing help
    


    # Taking input guess from user
    while(True):
        try:
            hint_needed = input('Do you want a hint![y/n]')
            if(hint_needed == 'y'):
                print('hint: the number is close to ', random_num - 10)
            user_guess = int(input(f'Guess a number between {start} and {stop}: '))
            if(user_guess < start or user_guess > stop):
                raise OutOfRangeError
        except ValueError:
            print('please enter an integer')
            
        except OutOfRangeError:
            print(f'please enter an integer between {start} and {stop}')
        else:
            break

    
    # Checking if user guessed it correct! Else asking again till in tries remain
    if(random_num == user_guess):
        print('You are a genius! Well guessed!!')
        break
    else:
        print('oops!! Wrong guess. Please try again')
        count+=1
        print('Remaining tries: ', 10 - count)
    if(count == 10):
        print('You just exhausted your try limit!! Please start a new game.')
        break

# Function end


# To test
if (__name__ == '__main__'):
    game()
# print(__name__)