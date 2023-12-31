# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


names = []

with open("Input/Names/invited_names.txt", "r") as invited_names:
    names_raw = invited_names.readlines()
for name in names_raw:
    names.append(name.strip("\n"))

with open("Input/Letters/starting_letter.txt", "r") as starting_letter:
    letter = starting_letter.read()
    for name in names:
        new_letter = letter.replace("[name]", name)
        with open(f"Output/ReadyToSend/{name}.txt", "w") as to_send:
            to_send.write(new_letter)

