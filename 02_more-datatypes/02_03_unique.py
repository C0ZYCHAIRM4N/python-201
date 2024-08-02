# Write code that creates a list of all unique values in a list.
# For example:
#
# list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
# unique_list = [55, 'hi', 4, 13]

# Original list
list_ = [1, 2, 3, "hello", 1, 39, 2, 5, "hello", 2.4, 2.4, 3]

# Create a list of unique values
unique_list = [item for item in list_ if list_.count(item) == 1]

print(unique_list)


