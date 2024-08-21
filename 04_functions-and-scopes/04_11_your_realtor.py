# Write a function that prints out nicely formatted information about a
# real estate advertisement. The information can vary for every advertisement, which
# is why your function should be able to take an arbitrary amount of
# keyword arguments, and display them all in a list form with some 
# introductory information.
def realtor(**kwargs):
    print("New real estate advertisement:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
# Call the function with the following keyword arguments:
# - `location`: "San Francisco"
# - `price`: "$1,000,000"
# - `rooms`: 3
# - `bathrooms`: 2
# - `pool`: True
realtor(location="San Francisco", price="$1,000,000", rooms=3, bathrooms=2, pool=True)