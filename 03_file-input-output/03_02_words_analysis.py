# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.
# Open the file and read all words into a list
file_input = open(r"C:\Users\speng\OneDrive\Desktop\codingnomads 201 labs\python-201\03_file-input-output\words.txt", 'r')
words = file_input.read().split()

# Initialize variables to store the shortest and longest words
shortest_words = []
longest_words = []
min_length = float('inf')
max_length = 0

# Iterate through each word to find the shortest and longest words
for word in words:
    word_length = len(word)
    
    # Check for shortest word
    if word_length < min_length:
        shortest_words = [word]
        min_length = word_length
    elif word_length == min_length:
        shortest_words.append(word)
    
    # Check for longest word
    if word_length > max_length:
        longest_words = [word]
        max_length = word_length
    elif word_length == max_length:
        longest_words.append(word)

# Print the results
print("Shortest word(s):", shortest_words)
print("Longest word(s):", longest_words)
print("Total number of words:", len(words))

   