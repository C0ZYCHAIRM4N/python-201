# How can you call the function defined below using the given
# dictionary as its input.
# You shouldn't explicitly access the dict values, but use
# dictionary unpacking when passing the argument instead.

def congratulate(name, age):
    return f"Today {name} is {age} years old.\nHappy Birthday!"

user = {"name": "Adelheid", "age": 22}
congratulate(**user)
# Expected output:
# Today Adelheid is 22 years old.
print(congratulate(**user))
