class calculscores:
    def __init__(self):
        self._scoreJ1 = 0
        self._scoreJ2 = 0
        self._scoreJ3 = 0
        self._scoreJ4 = 0

    def calculscore(self, joueur, points):
        if joueur == 1:
            self._scoreJ1 += points
        elif joueur == 2:
            self._scoreJ2 += points
        elif joueur == 3:
            self._scoreJ3 += points
        elif joueur == 4:
            self._scoreJ4 += points

    def score(self):
        return self._scoreJ1, self._scoreJ2, self._scoreJ3, self._scoreJ
