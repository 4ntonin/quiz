class calculScores:
    def __init__(self):
        self.__joueuractif = 0
        self.__scoreJ1 = 0
        self.__scoreJ2 = 0
        self.__scoreJ3 = 0
        self.__scoreJ4 = 0
    
    def set_joueur(self, joueur):
        self.__joueuractif = joueur
    
    def get_joueur(self):
        return self.__joueuractif

    def calcul_score(self, points):
        if self.__joueuractif == 1:
            self.__scoreJ1 += points
        elif self.__joueuractif == 2:
            self.__scoreJ2 += points
        elif self.__joueuractif == 3:
            self.__scoreJ3 += points
        elif self.__joueuractif == 4:
            self.__scoreJ4 += points

    def get_scores(self):
        return self.__scoreJ1, self.__scoreJ2, self.__scoreJ3, self.__scoreJ4
    
    def valider(self):
        """Valide la réponse du joueur et appelle calcul_score pour distribuer les points"""
        return self.calcul_score(1)


# Voilà comment on va procéder dans le programme principal

# c = calculScores()
# j1, j2, j3, j4 = c.get_scores()
# print(j1, j2, j3, j4)
# c.set_joueur(1)
# c.calcul_score(1)
# j1, j2, j3, j4 = c.get_scores()
# print(j1, j2, j3, j4)
# c.set_joueur(3)
# c.valider()
# j1, j2, j3, j4 = c.get_scores()
# print(j1, j2, j3, j4)
