"""
Il faudra utiliser cette classe dans le fichier principal du jeu
Actuellement, beaucoup de fichiers sont reliés à la base de données 'test',
il faudra les lier à la base de données principale ('BDDQuiz') lors de
l'intégration complète du jeu.
"""

import BDD
from random import randint


class Tirage:
    def __init__(self, theme):
        self.base = BDD.BDD("test")

        self.base.requetesql("SELECT id from {}".format(str(theme)))
        self.ids = [i[0] for i in self.base.get_cursor().fetchall()]

    def pick_random_id(self):
        i = randint(0, len(self.ids) - 1)
        picked_id = self.ids[i]
        self.ids.pop(i)
        return picked_id
