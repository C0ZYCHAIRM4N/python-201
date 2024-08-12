# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.

def greet(use):
    return f"Hello {use}!"

def write_letter(name, text):
    greeting = greet(name)
    goodbye = f"\n\nSincerely,\n{name}"
    letter = greeting + text + goodbye
    return letter
letter = write_letter("Alice", "I hope this letter finds you well.")
print(letter)