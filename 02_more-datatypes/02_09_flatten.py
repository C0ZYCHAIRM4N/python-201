# Write a script that "flattens" a shallow list. For example:
#
# starter_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Note that your input list only contains one level of nested lists.
# This is called a "shallow list".
#
# CHALLENGE: Do some research online and find a solution that works
# to flatten a list of any depth. Can you understand the code used?

starter_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = [item for sublist in starter_list for item in sublist]
print(flattened_list)

# recursive function
def flatten_list(nested_list):
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened
nested_list = [[1, [2, 3]], [4, [5, [6, 7]]], [8, 9]]

# Flatten the nested list
flattened_list = flatten_list(nested_list)

print(f"Flattened list: {flattened_list}")