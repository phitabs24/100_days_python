# Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
all_names = []

with open("./Input/Letters/starting_letter.txt") as letter:
    STARTING_LETTER = letter.read()

with open("./Input/Names/invited_names.txt") as names:
    invitees = names.readlines()
for line in invitees:
    name = line.strip()
    all_names.append(name)
    new_letter = STARTING_LETTER.replace("[name]", name, 1)
    with open(f"./Output/ReadyToSend/letter_for_{name}.docx", mode="w") as final:
        final.write(new_letter)
