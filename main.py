import random


fichier = open("motsaa.txt", 'r', encoding="utf-8")
facile = []
moyen = []
difficile = []


for line in fichier:
    if len(line[:-1])<5:
        facile.append(line[:-1].lower())
    elif len(line[:-1])<10:
        moyen.append(line[:-1].lower())
    else:
        difficile.append(line[:-1].lower())


difficulty = str(input("Veuillez choisir une difficulté : facile, moyen, difficile \n"))


if difficulty == "facile":
    chosen_word = random.choice(facile)
elif difficulty == "moyen":
    chosen_word = random.choice(moyen)
elif difficulty == "difficile":
    chosen_word = random.choice(difficile)




find_word = []

occurence = {}

for letter in chosen_word:
    occurence[letter] = 0
for letter in chosen_word:
    occurence[letter] += 1
compteur = 0


for letter in chosen_word:

    if occurence[letter] == 1 and compteur !=1:
        find_word += letter
        compteur += 1
    else:
        find_word += "_"



Ingame = True
print(occurence)

print(chosen_word)

chosen_word = list(chosen_word)
"""
print(chosen_word)
print(find_word)
"""





while Ingame:
    word = str(input("Veuillez choisir une lettre ou un mot : "))

    for i in range(len(chosen_word)):
        for j in range(len(find_word)):
            if chosen_word[i] == word:
                find_word[i] = chosen_word[i]
    if find_word == chosen_word or word == "".join(chosen_word):
        find_word = chosen_word
        print("Vous avez gagné")
        Ingame = False


    #print(find_word)
    print("".join(find_word))




