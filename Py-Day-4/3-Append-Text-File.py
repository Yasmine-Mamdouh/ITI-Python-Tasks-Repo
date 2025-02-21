# Append Text to an Existing File

# Open a text file in append mode.
# Add new content without overwriting the existing text.

append_text = "\nI am a System Admin Student at ITI."

with open("text.txt", "a") as file:
    file.write(append_text)

with open("text.txt", "r") as file:
    contents = file.read()

print(contents)
