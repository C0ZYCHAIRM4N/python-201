# Write a script that takes a string from the user
# and creates a list that contains a tuple for each word.
# For example:

# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

user_input = input("enter a string: ")
words = user_input.split()

result = [tuple(word) for word in words]
print(result)
