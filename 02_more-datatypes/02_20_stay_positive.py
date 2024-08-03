# Use a list comprehension to create a list called `positive` from the list
# `numbers` that contains only the positive numbers from the provided list.

numbers = [5, -8, 3, 10, -19, -22, 44, 2, -1, 4, 42]
positive = [x for x in numbers if x > 0]
print(positive)
