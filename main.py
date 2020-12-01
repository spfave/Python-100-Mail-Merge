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


# Functions
def write_letter(file_path, file_name, text):
    """ Write input text to file file_name at file_path """

    with open(file_path+file_name, mode="w") as file:
        file.write(text)


# Main
with open(PATH_LETTER_TEMPLATE+"starting_letter.docx", mode="r") as file:
    letter_template = file.read()


with open(PATH_INVITEES+"invited_names.txt", mode="r") as file:
    invite_names = file.readlines()


for name in invite_names:
    name_formated = name.strip()
    letter_file_name = f"Letter to {name_formated}.docx"
    letter_text = letter_template.replace("[name]", name_formated)
    write_letter(PATH_READY_LETTERS, letter_file_name, letter_text)
