from tkinter import *
from functools import *
from calcul_scores import *

j1 = 0
j2 = 0
j3 = 0
j4 = 0

def test():
    global app
    app = Tk()
    app.title("Scores")

    window_height = 768
    window_width = 1024
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    app.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

    l = LabelFrame(app, background="#ffcccc", padx=10, pady=100)
    l.pack(fill="both", expand="yes")

    FrameScore1 = LabelFrame(l, text=['Score', 'joueur', '1:'], font=("Unispace", 16), background="#ffcccc", padx=20, pady=20)
    FrameScore1.pack(side=TOP, padx=5, pady=5)
    s1= Label(FrameScore1, text=j1, width=50, background="#ffcccc", font=("Unispace",16))
    s1.pack()

    FrameScore2 = LabelFrame(l, text=['Score', 'joueur', '2:'], font=("Unispace", 16), background="#ffcccc", padx=20, pady=20)
    FrameScore2.pack(side=TOP, padx=5, pady=5)
    s1= Label(FrameScore2, text=j2, width=50, background="#ffcccc", font=("Unispace",16))
    s1.pack()

    FrameScore3 = LabelFrame(l, text=['Score', 'joueur', '3:'], font=("Unispace", 16), background="#ffcccc", padx=20, pady=20)
    FrameScore3.pack(side=TOP, padx=5, pady=5)
    s3= Label(FrameScore3, text=j3, width=50, background="#ffcccc", font=("Unispace",16))
    s3.pack()

    FrameScore4 = LabelFrame(l, text=['Score', 'joueur', '4:'], font=("Unispace", 16), background="#ffcccc", padx=20, pady=20)
    FrameScore4.pack(side=TOP, padx=5, pady=5)
    s4= Label(FrameScore4, text=j4, width=50, background="#ffcccc", font=("Unispace",16))
    s4.pack()

    #Text=StringVar()
    #entry=Entry(l,textvariable=Text,font=('Unispace',16),width=40)
    #entry.pack(side=TOP, padx=5,pady=5)

    #Bouton=Button(l, text='Refresh',font=('Unispace',16), background="#ffcccc", padx=50, pady=10)
    #Bouton.pack(side=TOP, padx=5,pady=5)


    app.mainloop()

#def refresh():
    #lab.destroy()
    #c.set_joueur(getJoueur())
    #j1, j2, j3, j4 = c.get_scores()
    #c.valider()
    #test()

def getJoueur():
    res = 0
    return res

def main():
    global lab
    lab = Tk()
    lab.title('Scores')
    lab.resizable(width=True, height=False)
    paned = PanedWindow(lab, handlesize=6, height=300, width=1560, showhandle=False, sashrelief='sunken')
    l1 = Label(paned, text=['Score', 'joueur', '1:', j1], height=500, background="white", font=("Unispace", 20))
    l2 = Label(paned, text=['Score', 'joueur', '2:', j2], height=500, background="white", font=("Unispace", 20))
    l3 = Label(paned, text=['Score', 'joueur', '3:', j3], height=500, background="white", font=("Unispace", 20))
    l4 = Label(paned, text=['Score', 'joueur', '4:', j4], height=500, background="white", font=("Unispace", 20))
    paned.add(l1, height=300, width=260, sticky="ew")
    paned.add(l2, height=300, width=260, sticky="ew")
    paned.add(l3, height=300, width=260, sticky="ew")
    paned.add(l4, height=300, width=260, sticky="ew")
    paned.grid(sticky="ew", row=20, column=10, rowspan=2)
    lab.grid_columnconfigure(10, weight=1)
    text = IntVar(lab)
    entry = Entry(lab, textvariable=text, text=['Joueur', 'actif'], font=("Unispace", 20))
    l5= entry
    paned.add(l5,height=300,width=180,sticky="w")
    l6= Button(lab,text='Refresh',command=refresh, font=("Unispace", 10),background="#ffcccc")
    paned.add(l6,height=300,width=200,sticky='w')
    paned.grid(sticky="w", row=20, column=10, rowspan=2)
    lab.mainloop()


c=calculScores()
test()
#main()
#while sj1<40 and sj2<40 and sj3<40 and sj4 <40:
    #a.main()
