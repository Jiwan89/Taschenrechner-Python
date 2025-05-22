import tkinter as tk

def klick(symbol):
    eingabe_feld.insert(tk.END, symbol)

def berechne():
    try:
        ergebnis = eval(eingabe_feld.get())
        eingabe_feld.delete(0, tk.END)
        eingabe_feld.insert(tk.END, str(ergebnis))
    except:
        eingabe_feld.delete(0, tk.END)
        eingabe_feld.insert(tk.END, "Fehler")

def löschen():
    eingabe_feld.delete(0, tk.END)

# Fenster
fenster = tk.Tk()
fenster.title("Taschenrechner")

# Eingabefeld
eingabe_feld = tk.Entry(fenster, width=20, font=("Arial", 16), bd=5, relief="ridge", justify="right")
eingabe_feld.grid(row=0, column=0, columnspan=4)

# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

reihe = 1
spalte = 0

for button in buttons:
    def cmd(b=button):
        if b == "=":
            berechne()
        else:
            klick(b)
    tk.Button(fenster, text=button, width=5, height=2, command=cmd).grid(row=reihe, column=spalte)
    spalte += 1
    if spalte > 3:
        spalte = 0
        reihe += 1

tk.Button(fenster, text="C", width=5, height=2, command=löschen).grid(row=reihe, column=0)

fenster.mainloop()
