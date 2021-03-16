import utility # our self made module  # Better practice than directly importing function
print(utility.multiply(2,3))
print(utility.divide(2,3))

#  from utility import * # not a good practice since original functions can be overridden

import shopping.shopping_cart # Method 1 to import from our own package
print(shopping.shopping_cart)

from shopping import shopping_cart # Method 2 to import from our own package
print(shopping_cart)

from shopping.shopping_cart import buy
print(buy('apple'))

from utility import multiply
print(multiply(2,4))
# print(divide(2,4)) # This will throw an error since we just import the multiply function

from shopping.more_shopping import cost # Better practice than directly importing function
print(cost)
print(cost.get_cost('apple'))

from shopping.more_shopping.cost import get_cost
print(get_cost('pear'))