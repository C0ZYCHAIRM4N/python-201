# Write a script that takes a text input from the user
# and creates a dictionary that maps the letters in the string
# to the number of times they occur. For example:
#
# user_input = "hello"
# result = {"h": 1, "e": 1, "l": 2, "o": 1}
# Get input from the user
user_input = input("Enter a string: ")

# Create an empty dictionary to store the result
result = {}

# Iterate over the characters in the string
for char in user_input:
    # If the character is already in the dictionary, increment its value
    if char in result:
        result[char] += 1
    else:
        # If the character is not in the dictionary, add it with a value of 1
        result[char] = 1

# Print the result
print(result)