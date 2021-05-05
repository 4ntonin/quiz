from tkinter import *
from functools import *
from calcul_scores import *


scoreJ1 = 0
scoreJ2 = 0
scoreJ3 = 0
scoreJ4 = 0


def main():
    global lab
    lab = Tk()
    lab.title('Scores')
    lab.resizable(width=True, height=False)
    paned = PanedWindow(lab, handlesize=6, height=300, width=1560, showhandle=False, sashrelief='sunken')
    l1 = Label(paned, text=['Score', 'joueur', '1:', scoreJ1], height=500, background="white", font=("Unispace", 20))
    l2 = Label(paned, text=['Score', 'joueur', '2:', scoreJ2], height=500, background="white", font=("Unispace", 20))
    l3 = Label(paned, text=['Score', 'joueur', '3:', scoreJ3], height=500, background="white", font=("Unispace", 20))
    l4 = Label(paned, text=['Score', 'joueur', '4:', scoreJ4], height=500, background="white", font=("Unispace", 20))
    paned.add(l1, height=300, width=300, sticky="ew")
    paned.add(l2, height=300, width=300, sticky="ew")
    paned.add(l3, height=300, width=300, sticky="ew")
    paned.add(l4, height=300, width=300, sticky="ew")
    paned.grid(sticky="ew", row=20, column=10, rowspan=2)
    lab.grid_columnconfigure(10, weight=1)
    text = IntVar(lab)
    j=text
    entry = Entry(lab, textvariable=text, text=['Joueur', 'actif'], font=("Unispace", 20))
    l5= entry
    paned.add(l5,height=300,width=200,sticky="w")
    l6= Button(lab,text='Refresh',command=refresh, font=("Unispace", 10),background="#ffcccc")
    paned.add(l6,height=300,width=1500,sticky='w')
    paned.grid(sticky="w", row=20, column=10, rowspan=2)
    lab.mainloop()
    return text


#def getEntry():
    #res= main
    #return res
def refresh(j):
    lab.destroy()
    c.set_joueur(j)
    j1, j2, j3, j4 = c.get_scores()
    c.valider()
    print(j1, j2, j3, j4)
    main()

c=calculScores()
main()
#while sj1<40 and sj2<40 and sj3<40 and sj4 <40:
    #a.main()
