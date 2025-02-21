# Merge the Contents of Two Files into a Third File

# Open two text files and read their contents.
# Write the combined contents into a third file.

with open("text.txt", "r") as file1, open("test.txt", "r") as file2:
    contents1 = file1.read()
    contents2 = file2.read()

with open("merged.txt", "w") as merged_file:
    merged_file.write(contents1 + "\n" + contents2)

with open("merged.txt", "r") as file:
    contents = file.read()

print(contents)
