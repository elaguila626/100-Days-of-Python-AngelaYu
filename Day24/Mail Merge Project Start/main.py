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






