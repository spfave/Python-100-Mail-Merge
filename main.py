# TODO: Create a letter using starting_letter.docx
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# Constants
PATH_LETTER_TEMPLATE = "./Input/Letters/"
PATH_INVITEES = "./Input/Names/"
PATH_READY_LETTERS = "./Output/ReadyToSend/"


# Main
with open(PATH_LETTER_TEMPLATE+"starting_letter.docx", mode="r") as file:
    letter_template = file.read()

print(letter_template)
