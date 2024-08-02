# Take in a few numbers from the user and place them in a list.
# If you want, you can instead use the provided randomly generated
# list called `randlist` to simulate the user input.
#
# Find the largest number in the list and print the result.
# Calculate the product of all of the numbers in the list.
import math
from resources import randlist

largest_number = max(randlist)
print(largest_number)
product = math.prod(randlist)
print(product)



