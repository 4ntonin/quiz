from tkinter import *
from tkinter.messagebox import *
import BDD


base = BDD.BDD("BDDQuiz")

app = Tk()
app.title("Enregistrement des questions")

window_height = 768
window_width = 1024
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (window_height / 2))
app.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")


def alert():
    showinfo("alerte", "Bravo!")


def ajouter_theme():
    theme = nt.get()
    base.requetesql("CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, question TEXT, reponse TEXT)".format(str(theme)))


def ajouter_q_r():
    theme = str(t.get())
    question = str(q.get())
    reponse = str(r.get())
    base.requetesql("INSERT INTO {} (question, reponse) VALUES (?, ?)".format(theme), (question, reponse))


menubar = Menu(app)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Créer", command=alert)
menu1.add_command(label="Editer", command=alert)
menu1.add_separator()
menu1.add_command(label="Quitter", command=app.quit)
menubar.add_cascade(label="Fichier", menu=menu1)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=alert)
menubar.add_cascade(label="Aide", menu=menu3)

app.config(menu=menubar)


l = LabelFrame(app, background="#ffcccc", padx=20, pady=20)
l.pack(fill="both", expand="yes")

###############################################################################
FrameTheme = LabelFrame(l, text="Thème", font=("Unispace", 16), background="#ffcccc", padx=20, pady=20)
FrameTheme.pack(side=TOP, padx=5, pady=30)

OptionList = base.get_tables()

t = StringVar(FrameTheme)
if OptionList == []:
    t.set("Pas de thème disponible.")
    opt = OptionMenu(FrameTheme, t, "Pas de thème disponible.")
else:
    t.set(OptionList[0])
    opt = OptionMenu(FrameTheme, t, *OptionList)

opt.config(width=50, background="#ffcccc")
opt.pack()


def nouveau_theme():
    apptheme = Tk()
    apptheme.title("Enregistrer un thème")
    window_height = 400
    window_width = 800
    screen_width = apptheme.winfo_screenwidth()
    screen_height = apptheme.winfo_screenheight()
    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    apptheme.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

    ltheme = LabelFrame(apptheme, background="#ffcccc", padx=20, pady=40)
    ltheme.pack(fill="both", expand="yes")

    FrameNewTheme = LabelFrame(ltheme, text="Nouveau thème", font=("Unispace", 16), background="#ffcccc", padx=20, pady=20)
    FrameNewTheme.pack(side=TOP, padx=5, pady=30)

    global nt
    nt = Entry(FrameNewTheme, width=100)
    nt.pack()

    bouton = Button(ltheme, text="Valider", command=ajouter_theme, font=("Unispace", 16), background="#ffcccc", padx=20, pady=5)
    bouton.pack(pady=30)


bouton = Button(FrameTheme, text="Ajouter un thème", command=nouveau_theme, font=("Unispace"), background="#ffcccc", padx=15, pady=5)
bouton.pack(pady=30)

###############################################################################
FrameQuestion = LabelFrame(l, text="Question", font=("Unispace", 16), background="#ffcccc", padx=20, pady=20)
FrameQuestion.pack(side=TOP, padx=5, pady=30)

q = Entry(FrameQuestion, width=100)
q.pack()

###############################################################################
FrameReponse = LabelFrame(l, text="Réponse", font=("Unispace", 16), background="#ffcccc", padx=20, pady=20)
FrameReponse.pack(side=TOP, padx=5, pady=30)

r = Entry(FrameReponse, width=100)
r.pack()

###############################################################################
bouton = Button(l, text="Valider", command=ajouter_q_r, font=("Unispace", 16), background="#ffcccc", padx=20, pady=5)
bouton.pack(pady=30)

app.mainloop()
