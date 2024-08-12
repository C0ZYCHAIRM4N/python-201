# Write a program with three functions. Each function must call
# at least one other function and use the return value
# of that function to do something with it. You can have more
# than three functions, and they don't need to call each other
# in a circular way.
def first_function():
    return "Hello"
def second_function():
    example = first_function()
    return example + " World"
def third_function():
    example2 = second_function()
    return example2 + "!"
print(third_function())