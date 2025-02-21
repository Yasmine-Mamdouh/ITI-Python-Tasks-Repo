# Write to a Text File

# Open a text file in write mode.
# Write a given string to the file.
# If the file does not exist, create it.

new_text = "Hello, I am Yasmine"

with open("text.txt", "w") as file:
    file.write(new_text)

with open("text.txt", "r") as file:
    contents = file.read()

print(contents)
