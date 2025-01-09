import random

import difficulty

class Game:

    def __init__(self):
        self.find_word = []
        self.ingame = True
        self.difficultys = difficulty.Difficulty(difficulty)
        self.occurence = {}
        self.chosen_word = self.choose_word()

    def choose_word(self):
        self.difficultys.fill_word()
        chosen_word = ""
        if self.difficultys.difficulty == "facile":
            chosen_word = random.choice(self.difficultys.facile)
        elif self.difficultys.difficulty == "moyen":
            chosen_word = random.choice(self.difficultys.moyen)
        elif self.difficultys.difficulty== "difficile":
            chosen_word = random.choice(self.difficultys.difficile)
        else:
            self.difficultys.asked_difficulty()


        return chosen_word



    def letter_occurence(self):
        """
        create a list of the number of occurrences of each letter in the chosen word,
        thereby revealing only the letter that appears only once.

        """
        for letter in self.chosen_word:
            self.occurence[letter] = 0
        for letter in self.chosen_word:
            self.occurence[letter] += 1
        compteur = 0

        for letter in self.chosen_word:

            if self.occurence[letter] == 1 and compteur != 1:
                self.find_word += letter
                compteur += 1
            else:
                self.find_word += "_"


    def play(self):
        self.letter_occurence()
        chosen_word = list(self.chosen_word)
        error = 0
        while self.ingame:
            print("Le mot à deviner : " + "".join(self.find_word))
            word = str(input("Veuillez choisir une lettre ou un mot : "))
            if word not in chosen_word:
                error += 1
            if word == "".join(self.chosen_word):
                error -= 1

            for i in range(len(chosen_word)):
                if chosen_word[i] == word:
                    self.find_word[i] = chosen_word[i]

            print(f"Erreur : {error}")

            if self.find_word == chosen_word or word == "".join(chosen_word):
                self.find_word = chosen_word
                print(f"Vous avez gagné, le mot était bien : {"".join(self.find_word)}")
                replay = str(input("Voulez vous rejouer ? oui/non \n "))
                good_choice = True
                while good_choice:
                    if replay == "non":

                        self.ingame = False
                        break

                    if replay == "oui":

                        error = 0
                        self.occurence = {}
                        self.find_word = []
                        self.chosen_word = self.choose_word()
                        self.play()
                        good_choice = False
                    else:
                        replay = str(input("Voulez vous rejouer ? oui/non \n "))




