# Use the union operator `|` to combine the two given sets
# inside of a set comprehension that squares each item of the
# set if the number is higher than `2`.
# You should write the whole code logic in only one line.
#
# Expected output: {16, 9, 25, 49}
#
# Remember that sets are unordered collections, so your numbers
# might come out in a different order.

s = {1, 2, 3, 4}
t = {2, 3, 4, 5, 7}
new_set = {x**2 for x in s | t if x > 2}
print(new_set)