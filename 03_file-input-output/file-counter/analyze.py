import csv

# Open the CSV file
with open('words.txt', 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)

    # Create a dictionary to store the file types and their counts
    file_types = {}

    # Iterate over each row in the CSV file
    for row in reader:
        # Get the file type from the row
        file_type = row[0]  # Assuming the file type is in the first column

        # Check if the file type already exists in the dictionary
        if file_type in file_types:
            # If it exists, increment the count by 1
            file_types[file_type] += 1
        else:
            # If it doesn't exist, add it to the dictionary with a count of 1
            file_types[file_type] = 1

# Print the file types and their counts
for file_type, count in file_types.items():
    print(f'{file_type}: {count}')
