# The code below contains a few bugs. Use your debugger to find and fix them.

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = []

for x in range(1, len(unsorted_list)):

    minimum = unsorted_list[0][0]
    index = 0

    for i in range(1, len(unsorted_list)):
        if unsorted_list[i][1] < minimum:
            minimum = unsorted_list[i][i]
            index = i
    sorted_list.append(unsorted_list[index])
    unsorted_list.remove(unsorted_list[index])


print(sorted_list)
