class calculScores:
    def __init__(self):
        self.__scoreJ1 = 0
        self.__scoreJ2 = 0
        self.__scoreJ3 = 0
        self.__scoreJ4 = 0

    def calcul_score(self, joueur, points):
        if joueur == 1:
            self.__scoreJ1 += points
        elif joueur == 2:
            self.__scoreJ2 += points
        elif joueur == 3:
            self.__scoreJ3 += points
        elif joueur == 4:
            self.__scoreJ4 += points

    def get_scores(self):
        return self.__scoreJ1, self.__scoreJ2, self.__scoreJ3, self.__scoreJ4
