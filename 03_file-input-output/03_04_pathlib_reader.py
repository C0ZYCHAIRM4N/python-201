from pathlib import Path
import csv

def count_files(directory):
    path = Path(directory)
    file_count = 0

    for file in path.iterdir():
        if file.is_file():
            file_count += 1

    return file_count

def write_to_csv(file_count, output_file):
    path = Path(output_file)

    with path.open(mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['File Count'])
        writer.writerow([file_count])

def main():
    directory = input("Enter the directory path: ")
    output_file = input("Enter the output file path: ")

    file_count = count_files(directory)
    write_to_csv(file_count, output_file)

if __name__ == "__main__":
    main()
