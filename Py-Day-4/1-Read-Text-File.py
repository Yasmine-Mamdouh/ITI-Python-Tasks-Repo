# Read a Text File

# Open a text file in read mode.
# Read and print its contents to the console.

with open("Py-Day-4-Task.txt", "r") as file:
    contents = file.read()

print(contents)
