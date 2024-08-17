# Create a Generator that loops over the given range and prints out only
# the items that are divisible by 1111.

nums = range(1, 1000000)
gen = (x for x in nums if x % 1111 == 0)
print(gen)
