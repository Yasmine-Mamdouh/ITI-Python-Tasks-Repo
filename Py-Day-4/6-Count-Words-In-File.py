# Count the Number of Words in a File

# Open a text file in read mode.
# Count and display the total number of words in the file.

with open("test.txt", "r") as file:
    contents = file.read()
    words = contents.split()
    word_count = len(words)

with open("test.txt", "r") as file:
    contents = file.read()

print(contents)
print(f"Number of words in the test.txt file: {word_count}")
