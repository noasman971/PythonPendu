class Difficulty:
    def __init__(self, difficulty):
        self.difficulty = self.asked_difficulty()
        self.fichier = open("mots.txt", 'r', encoding="utf-8")
        self.facile = []
        self.moyen = []
        self.difficile = []

    def fill_word(self):
        for line in self.fichier:
            if len(line[:-1])<5:
                self.facile.append(line[:-1].lower())
            elif len(line[:-1])<10:
                self.moyen.append(line[:-1].lower())
            else:
                self.difficile.append(line[:-1].lower())

    def asked_difficulty(self):
        good_choice = True
        difficulty = str(input("Veuillez choisir une difficulté : facile, moyen, difficile \n"))
        while good_choice:
            if difficulty not in ["facile", "moyen", "difficile"]:
                difficulty = str(input("Veuillez choisir une difficulté : facile, moyen, difficile \n"))
            else:
                good_choice = False
        return difficulty

