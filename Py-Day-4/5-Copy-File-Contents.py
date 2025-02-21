# Copy Contents from One File to Another

# Open a source file and read its contents.
# Write the contents to a new destination file.

with open("text.txt", "r") as source_file, open("test.txt", "w") as destination_file:
    source = source_file.read()
    destination_file.write(source)

with open("test.txt", "r") as file:
    contents = file.read()

print(contents)
