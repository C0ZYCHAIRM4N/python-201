# Use a one-liner list comprehension to express the following functionality:
#
# letters = []
# for letter in 'suchalongword':
#     letters.append(letter)
# print(letters)
listcomp = [letter for letter in 'suchalongword']
print(listcomp)
# Output: ['s', 'u', 'c', 'h', 'a', 'l', 'o', 'n', 'g', 'w', 'o', 'r', 'd']