# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:
# 1. Convert to a different data type
# 2. Use a loop and a second list to solve it more manually

list_ = [1, 2, 3, 4, 3, 4, 5]
no_duplicates = set(list_)
print(no_duplicates)

unique_list = []

for item in list_:
    if item not in unique_list:
        unique_list.append(item)
print(unique_list)

