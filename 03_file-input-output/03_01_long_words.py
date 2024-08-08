# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).

# open file
file_input = open(r"C:\Users\speng\OneDrive\Desktop\codingnomads 201 labs\python-201\03_file-input-output\words.txt", "r")


for line in file_input:
    words = line.split()
    for word in words:
        if len(word) > 20:
            print(word)
# Don't forget to close the file after you're done
file_input.close()

 




