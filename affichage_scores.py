from tkinter import *
from functools import *
from calcul_scores import *

score=calculScores
class AffScores():
    def __init__(self):
        self.scoreJ1 = 0
        self.scoreJ2 = 0
        self.scoreJ3 = 0
        self.scoreJ4 = 0


    def main(self):
        global lab
        lab = Tk()
        lab.title('Scores')
        lab.resizable(width=False, height=False)
        paned = PanedWindow(lab, handlesize=6, height=200, width=610, showhandle=False, sashrelief='sunken')
        l1 = Label(paned, text=['Score', 'joueur', '1:', self.scoreJ1], height=100, background="white", font=("Unispace", 10))
        l2 = Label(paned, text=['Score', 'joueur', '2:', self.scoreJ2], height=100, background="white", font=("Unispace", 10))
        l3 = Label(paned, text=['Score', 'joueur', '3:', self.scoreJ3], height=100, background="white", font=("Unispace", 10))
        l4 = Label(paned, text=['Score', 'joueur', '4:', self.scoreJ4], height=100, background="white", font=("Unispace", 10))
        paned.add(l1, height=200, width=150, sticky="ew")
        paned.add(l2, height=200, width=150, sticky="ew")
        paned.add(l3, height=200, width=150, sticky="ew")
        paned.add(l4, height=200, width=155, sticky="ew")
        paned.grid(sticky="ew", row=20, column=10, rowspan=2)
        lab.grid_columnconfigure(10, weight=1)
        lab.mainloop()

    def refresh(self,joueur,points):
        lab.destroy()
        score.set_joueur(joueur)
        score.valider()
        score.get_scores(1)
        self.scoreJ1=self.scorej1
        aff.main()

aff=AffScores
scores=calculScores
while sj1<40 and sj2<40 and sj3<40 and sj4 <40:
    main()
