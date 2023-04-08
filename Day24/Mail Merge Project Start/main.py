#TODO: Create a letter using starting_letter.txt

with open("./input/names/invited_names.txt","r") as name_list:
    names = []
    for name in name_list:
        name = name.strip()
        names.append(name)

with open("./input/letters/starting_letter.txt","r") as letter_content:
    letter = letter_content.read()
    # print(letter)
    name = letter.replace("[name]","Edwin")

for x in range(len(names)):
    name = letter.replace("[name]",names[x])
    with open("./output/readytosend/" f"letter_for_{names[x]}.txt", "w") as new_file:
        new_file.write(name)


# append each name into a list from invited_name file
# Open file with names and create a variable for the names
# Copy and paste the starting letter text in the main file
# Rotate through names in list (For Loop?)
# Save each letter written into Ready To Send foler as a text file

# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

#Practice run of how to create multiple files to a specific part of the directory
# for x in range(3):
#     print(x)
#     #filename = f"file_{x}.txt"
#     with open("./output/readytosend/"f"file_{x}.txt","w") as f:
#         f.write(letter)





