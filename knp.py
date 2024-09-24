import tkinter as tk
import random 

root = tk.Tk()
root.title("Kámen, nůžky, papír")


def kamen_f(pocitac):
    if pocitac == 0:
        vysl="Remíza"
    elif pocitac == 1:
        vysl="Vyhrál jsi"
    elif pocitac == 2:
        vysl="Prohrál jsi"
    vysledek = tk.Label(root, text=vysl)
    vysledek.grid(row=2, column=1)

def nuzky_f(pocitac):
    if pocitac == 0:
        vysl="Prohál jsi"
    elif pocitac == 1:
        vysl="Remíza"
    elif pocitac == 2:
        vysl="Vyhrál jsi"
    vysledek = tk.Label(root, text=vysl)
    vysledek.grid(row=2, column=1)

def papir_f(pocitac):
    if pocitac == 0:
        vysl="Vyhrál jsi"
    elif pocitac == 1:
        vysl="Prohrál jsi"
    elif pocitac == 2:
        vysl="Remíza"
    vysledek = tk.Label(root, text=vysl)
    vysledek.grid(row=2, column=1)



pocitac=random.randrange(0,3)

#0=kamen
#1=nuzky
#2=papir


vyber= tk.Label(root, text="Vyber si")
vyber.grid(row=0, column=1)

kamen = tk.Button(root, text="Kámen", font="Arial 20", padx=20, pady=20, command=lambda:kamen_f(pocitac))
kamen.grid(row=1, column=0)

nuzky = tk.Button(root, text="Nůžky", font="Arial 20", padx=20, pady=20, command=lambda:nuzky_f(pocitac))
nuzky.grid(row=1, column=1)

papir = tk.Button(root, text="Papír", font="Arial 20", padx=20, pady=20, command=lambda:papir_f(pocitac))
papir.grid(row=1, column=2)


root.mainloop()
