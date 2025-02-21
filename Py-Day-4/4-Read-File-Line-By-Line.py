# Read a File Line by Line with Line Numbers

# Open a text file and read it line by line.
# Print each line along with its corresponding line number.

with open("Py-Day-4-Task.txt", "r") as file:
    line_number = 1
    for line in file:
        print(f"Line number {line_number} says: {line.strip()}")
        line_number += 1
