import BDD
from random import randint


class Tirage:
    def __init__(self):
        self.base = BDD.BDD("BDDQuiz")

    def get_question(self, theme):
        self.base.requetesql("SELECT question from {}".format(str(theme)))
        question = [i[0] for i in self.base.get_cursor().fetchall()]
        return question

    def pick_random_question(self, theme):
        question = self.get_question(theme)
        return question[randint(0, len(question) - 1)]
