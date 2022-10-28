import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dic = {row.letter: row.code for (index, row) in data.iterrows()}

to_continue = True
while to_continue:
    name = input("Enter the name: ").upper()
    try:
        result = [nato_dic[character] for character in name]
    except KeyError:
        print("Only letters in the alphabet are allowed!")
    else:
        print(result)
    finally:
        option = input("Do you want to continue y|n: ").lower()
        if option != "y":
            to_continue = False
