# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats():
  list_max = max(example_list)
  list_min = min(example_list)
  list_avg = sum(example_list) / len(example_list)
  list_sum = sum(example_list)
  print(f"Max: {list_max}")
  print(f"Min: {list_min}")
  print(f"Avg: {list_avg}")
  print(f"Sum: {list_sum}")
# define the function here
Operations_on_nums = stats()
print(Operations_on_nums)

# call the function below here
