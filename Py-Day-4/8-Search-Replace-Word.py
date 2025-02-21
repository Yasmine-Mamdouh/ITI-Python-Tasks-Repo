# Search and Replace a Word in a File

# Open a text file and search for a specific word.
# Replace all occurrences of the word with another word.
# Save the modified content back to the file.

search_for = "ITI"
replace_with = "ITI Alex Branch"

with open("text.txt", "r") as file:
    old_contents = file.read()

print('The old content is: \n' + old_contents)

updated_contents = old_contents.replace(search_for, replace_with)

with open("text.txt", "w") as file:
    file.write(updated_contents)

print('\nThe updated content is: \n' + updated_contents)
