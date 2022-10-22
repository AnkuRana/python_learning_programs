#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

FILEPATH = "./Input/Names/invited_names.txt"
names = []


def get_name(filepath):
    name_list = []
    with open(f"{filepath}", mode="r") as file:
        for line in file:
            name_list.append(line.strip())
    return name_list


def write_letter(name):
    path = f"./Output/ReadyToSend/letter_to_{name}.txt"
    with open(path, mode="w") as letter:
        with open("./Input/Letters/starting_letter.txt", mode="r") as data:
            letter.write(data.read().replace("[name]", name))


names = get_name(FILEPATH)

for nam in names:
    write_letter(nam)
