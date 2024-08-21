# Define a function called `write_letter()` that takes as input a `name`
# and a `text` argument. In the body of the function, create a greeting
# message with the `name` input, as well as a goodbye message that uses
# the `name` again. Combine that with the input `text` to return a
# complete `letter`.
def write_a_letter(name, text):
    greeting = f"Dear {name},\n"
    goodbye = f"\nSincerely,\n{name}"
    letter = f"{greeting}\n{text}\n{goodbye}"
    return letter
# Call the function with your own name and a message of your choosing.
# Print the result to the console.
print(write_a_letter("John", "Hello, how are you?"))