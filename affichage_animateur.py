from tkinter import *
import tirage_question
import BDD

base = BDD.BDD("test")
# le theme sera choisi dans le programme principal et renvoyé ici
theme = "test1"
tirage = tirage_question.Tirage(theme)
# q_r = ()


def get_q_r():
    id = tirage.pick_random_id()
    base.requetesql("SELECT question, reponse FROM {} WHERE id = ?".format(theme), str(id))
    global q_r
    q_r = base.get_cursor().fetchone()


def main():
    get_q_r()

    global app
    app = Tk()
    app.title("Affichage animateur")

    window_height = 768
    window_width = 1024
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    app.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")


    l = LabelFrame(app, background="#ffcccc", padx=20, pady=120)
    l.pack(fill="both", expand="yes")

    # Affichage question
    FrameQuestion = LabelFrame(l, text="Question", font=("Unispace", 16), background="#ffcccc", padx=20, pady=20)
    FrameQuestion.pack(side=TOP, padx=5, pady=30)

    q = Label(FrameQuestion, text=q_r[0], width=75, background="#ffcccc", font=("Unispace"))
    q.pack()

    # Affichage réponse
    FrameReponse = LabelFrame(l, text="Réponse", font=("Unispace", 16), background="#ffcccc", padx=20, pady=20)
    FrameReponse.pack(side=TOP, padx=5, pady=30)

    r = Label(FrameReponse, text=q_r[1], width=75, background="#ffcccc", font=("Unispace"))
    r.pack()

    # bouton suivant (pas sûr de le garder celui-là)
    bouton = Button(l, text="Question suivante", command=refresh, font=("Unispace", 16), background="#ffcccc", padx=20, pady=5)
    bouton.pack(pady=30)

    app.mainloop()


def refresh():
    app.destroy()
    main()


main()
