# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.

while True:
    user_input = input("Enter a number please! ")
    
    try:
        number = int(user_input)
        print(f"You entered the number: {number}")
    except ValueError:
        print("Wrong input. Please enter a valid number.")
        break

    
    