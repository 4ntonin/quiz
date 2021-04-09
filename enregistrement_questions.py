from tkinter import *
from tkinter.messagebox import *
import BDD


base = BDD.BDD("test2")

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


def ajouter_theme(theme):
    base.requetesql(
        "CREATE TABLE IF NOT EXISTS ? (id INTEGER PRIMARY KEY AUTO INCREMENT UNIQUE, question TEXT, reponse TEXT)", theme)


def ajouter_q_r(theme, question, reponse):
    base.requetesql(
        "INSERT INTO ? (question, reponse) VALUES (?, ?)", (theme, question, reponse))


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
FrameTheme = LabelFrame(l, text="Thème", font=(
    "Unispace", 16), background="#ccf2ff", padx=20, pady=20)
FrameTheme.pack(side=TOP, padx=5, pady=30)

OptionList = base.get_tables()

variable = StringVar(FrameTheme)
if OptionList == []:
    variable.set("Pas de thème disponible.")
    opt = OptionMenu(FrameTheme, variable, "Pas de thème disponible.")
else:
    variable.set(OptionList[0])
    opt = OptionMenu(FrameTheme, variable, *OptionList)


opt.config(width=50, background="#ccf2ff")
opt.pack()

###############################################################################
FrameQuestion = LabelFrame(l, text="Question", font=(
    "Unispace", 16), background="#ccf2ff", padx=20, pady=20)
FrameQuestion.pack(side=TOP, padx=5, pady=30)

value = StringVar()
value.set("texte par défaut")
entree = Entry(FrameQuestion, width=100)
entree.pack()

###############################################################################
FrameReponse = LabelFrame(l, text="Réponse", font=(
    "Unispace", 16), background="#ccf2ff", padx=20, pady=20)
FrameReponse.pack(side=TOP, padx=5, pady=30)

value = StringVar()
value.set("texte par défaut")
entree = Entry(FrameReponse, width=100)
entree.pack()

###############################################################################
bouton = Button(l, text="Valider", command=app.quit, font=(
    "Unispace", 16), background="#ccf2ff", padx=20, pady=5)
bouton.pack(pady=30)


app.mainloop()
