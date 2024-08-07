# Write a script that takes the following two dictionaries
# and creates a new dictionary by combining the common keys
# and adding the values of duplicate keys together.
# Use `for` loops to iterate over these dictionaries
# to accomplish this task.
#
# Example output:
# result = {"a": 3, "b": 2, "c": 7 , "d": 2}

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

# Create an empty dictionary to store the result
result = {}

# Iterate over the keys in the first dictionary
for key in dict_1:
    # Check if the key is in both dictionaries
    if key in dict_2:
        # If the key is in both dictionaries, add the values together
        result[key] = dict_1[key] + dict_2[key]
    else:
        # If the key is only in the first dictionary, add it to the result
        result[key] = dict_1[key]

# Iterate over the keys in the second dictionary
for key in dict_2:
    # Check if the key is not already in the result (i.e., it's only in the second dictionary)
    if key not in result:
        result[key] = dict_2[key]

# Print the result
print(result)