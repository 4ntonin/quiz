from tkinter import *
from functools import *

sj1=0
sj2=1
sj3=10
sj4=12
root = Tk()
root.title('Scores')
root.resizable(width=False, height=False)
paned = PanedWindow(root, handlesize=6,height=200, width=610, showhandle=False, sashrelief='sunken')
l1 = Label(paned, text=['Score','joueur','1:',sj1], height=100, background="white",font=("Unispace",10))
l2 = Label(paned, text=['Score','joueur','2:',sj2], height=100, background="white",font=("Unispace",10))
l3 = Label(paned, text=['Score','joueur','3:',sj3], height=100, background="white",font=("Unispace",10))
l4 = Label(paned, text=['Score','joueur','4:',sj4], height=100, background="white",font=("Unispace",10))
paned.add(l1, height=200,width=150, sticky="ew")
paned.add(l2, height=200,width=150, sticky="ew")
paned.add(l3, height=200,width=150, sticky="ew")
paned.add(l4, height=200,width=155, sticky="ew")
paned.grid(sticky="ew", row=20, column=10,rowspan=2)
root.grid_columnconfigure(10, weight=1)
root.mainloop()