from tkinter import *
from tkinter.messagebox import *
import BDD


base = BDD.BDD("test")

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


def theme_ajoute():
    showinfo(message="Thème ajouté.")
    app.destroy()


def ajouter_theme(theme):
    theme = str(theme)
    base.requetesql("CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, question TEXT, reponse TEXT)".format(theme))
    theme_ajoute()


def ajouter_q_r(theme, question, reponse):
    base.requetesql("INSERT INTO Test1 (question, reponse) VALUES (?, ?)", (str(question), str(reponse)))


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


l = LabelFrame(app, background="#ccf2ff", padx=20, pady=20)
l.pack(fill="both", expand="yes")

###############################################################################
FrameTheme = LabelFrame(l, text="Thème", font=("Unispace", 16), background="#ccf2ff", padx=20, pady=20)
FrameTheme.pack(side=TOP, padx=5, pady=30)

OptionList = base.get_tables()

t = StringVar(FrameTheme)
t.set("[Thème]")
if OptionList == []:
    opt = OptionMenu(FrameTheme, t, "Pas de thème disponible.")
else:
    opt = OptionMenu(FrameTheme, t, *OptionList)


opt.config(width=50, background="#ccf2ff")
opt.pack()

###############################################################################
FrameQuestion = LabelFrame(l, text="Question", font=("Unispace", 16), background="#ccf2ff", padx=20, pady=20)
FrameQuestion.pack(side=TOP, padx=5, pady=30)

q = StringVar()
q.set("texte par défaut")
champ = Entry(FrameQuestion, width=100)
champ.pack()

###############################################################################
FrameReponse = LabelFrame(l, text="Réponse", font=("Unispace", 16), background="#ccf2ff", padx=20, pady=20)
FrameReponse.pack(side=TOP, padx=5, pady=30)

r = StringVar()
r.set("texte par défaut")
champ = Entry(FrameReponse, width=100)
champ.pack()

###############################################################################
bouton = Button(l, text="Valider", font=("Unispace", 16), background="#ccf2ff", command=ajouter_theme("Test7"), padx=20, pady=5)
bouton.pack(pady=30)

# ajouter_q_r(theme.get(), q.get(), r.get())

app.mainloop()
