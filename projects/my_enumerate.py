# Reproduce the functionality of Python's built-in `enumerate()` function.
# Define a function called `my_enumerate()` that takes an iterable as input
# and gives back both the element as well as its index position as an integer.

# Example list
fruits = ["apple", "banana", "cherry"]

# Using enumerate to loop over the list with an index
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

