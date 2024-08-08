# Write a script that reads in the contents of `words.txt`
# and writes the contents in reverse to a new file `words_reverse.txt`.
file_input = open(r"C:\Users\speng\OneDrive\Desktop\codingnomads 201 labs\python-201\03_file-input-output\words.txt", 'r')
contents = file_input.read()
reversed_content = contents[::-1]

with open(r"C:\Users\speng\OneDrive\Desktop\codingnomads 201 labs\python-201\03_file-input-output\words_reverse.txt", 'w') as file_output:
    file_output.write(reversed_contents)