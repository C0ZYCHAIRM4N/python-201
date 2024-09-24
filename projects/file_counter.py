# Add the code for the file counter script that you wrote in the course.
import csv

# Assuming you have a dictionary called 'file_counts' with file names as keys and their respective counts as values

file_counts = {
    'file1.txt': 10,
    'file2.txt': 5,
    'file3.txt': 7
}

# Specify the path and filename for the output CSV file
csv_file = '/c:/Users/speng/OneDrive/Desktop/codingnomads 201 labs/python-201/03_file-input-output/file-counter/file_counts.csv'

# Open the CSV file in write mode
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(['File Name', 'Count'])

    # Write the file counts
    for file_name, count in file_counts.items():
        writer.writerow([file_name, count])

print("File counts have been written to the CSV file."