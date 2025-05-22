# 📌 1. Importiere die Bibliothek tkinter und nenne sie "tk"
# Das brauchst du, um grafische Fenster zu bauen
import tkinter as tk

# 🧠 2. Funktion: Wird aufgerufen, wenn eine Zahl oder ein Symbol gedrückt wird (z. B. '7', '+', etc.)
def klick(symbol):
    # Schreibe das Symbol (z. B. "7" oder "+") am Ende des Eingabefelds
    # tk.END bedeutet: ganz am Ende einfügen
    eingabe_feld.insert(tk.END, symbol)

# 🧠 3. Funktion: Führt die Berechnung durch, wenn "=" gedrückt wird
def berechne():
    try:
        # Hole den aktuellen Text aus dem Eingabefeld (z. B. "2+3*4")
        ausdruck = eingabe_feld.get()

        # Evaluiere den mathematischen Ausdruck wie ein Taschenrechner
        # Beispiel: eval("2+3*4") → ergibt 14
        ergebnis = eval(ausdruck)

        # Lösche den aktuellen Inhalt im Eingabefeld
        eingabe_feld.delete(0, tk.END)

        # Zeige das Ergebnis im Eingabefeld an
        eingabe_feld.insert(tk.END, str(ergebnis))

    except:
        # Wenn ein Fehler passiert (z. B. durch ungültige Eingabe), zeige "Fehler"
        eingabe_feld.delete(0, tk.END)
        eingabe_feld.insert(tk.END, "Fehler")

# 🧠 4. Funktion: Löscht das Eingabefeld (wenn "C" gedrückt wird)
def löschen():
    eingabe_feld.delete(0, tk.END)

# 🖼️ 5. Erstelle das Hauptfenster der App
fenster = tk.Tk()  # neues Fenster-Objekt
fenster.title("Taschenrechner")  # Text oben in der Titelleiste

# ✏️ 6. Eingabefeld für Rechenausdruck
eingabe_feld = tk.Entry(
    fenster,              # Dieses Feld gehört zum Fenster
    width=20,             # Breite des Eingabefelds
    font=("Arial", 16),   # Schriftart und -größe
    bd=5,                 # Rahmenbreite des Felds
    relief="ridge",       # Rahmenstil (leicht erhaben)
    justify="right"       # Text wird rechtsbündig angezeigt
)
# Setze das Eingabefeld in die erste Zeile (row 0), über 4 Spalten (columnspan=4)
eingabe_feld.grid(row=0, column=0, columnspan=4)

# 🔘 7. Liste aller Taschenrechner-Buttons, die wir anzeigen wollen
buttons = [
    '7', '8', '9', '/',   # erste Reihe
    '4', '5', '6', '*',   # zweite Reihe
    '1', '2', '3', '-',   # dritte Reihe
    '0', '.', '=', '+'    # vierte Reihe
]

# 🧮 Startposition für das erste Button-Feld
reihe = 1   # Startreihe (unter dem Eingabefeld)
spalte = 0  # Startspalte (links)

# 🔁 8. Schleife, die für jedes Symbol einen Button erstellt
for button in buttons:
    # cmd-Funktion: Was soll beim Klicken passieren?
    def cmd(b=button):  # b=button ist wichtig, sonst geht nur der letzte Wert
        if b == "=":
            berechne()  # Wenn "=" gedrückt wurde → berechne das Ergebnis
        else:
            klick(b)    # Sonst → füge das Symbol ins Eingabefeld ein

    # Erstelle den Button mit Text und Befehl
    tk.Button(
        fenster,         # Der Button gehört zum Fenster
        text=button,     # Was drauf steht (z. B. "7")
        width=5,         # Breite des Buttons
        height=2,        # Höhe des Buttons
        font=("Arial", 14),  # Schrift im Button
        command=cmd      # Funktion, die bei Klick aufgerufen wird
    ).grid(row=reihe, column=spalte)  # Platziere den Button im Gitter

    # ➡️ Bewege dich zur nächsten Spalte
    spalte += 1
    if spalte > 3:
        # Wenn vier Spalten voll sind, fange in neuer Zeile an
        spalte = 0
        reihe += 1

# ❌ 9. Extra-Button "C" zum Löschen (Clear)
tk.Button(
    fenster,
    text="C",            # Text auf dem Button
    width=5,
    height=2,
    font=("Arial", 14),
    command=löschen      # Lösche bei Klick den Inhalt
).grid(row=reihe, column=0)  # Setze den C-Button in die nächste Zeile ganz links

# 🚀 10. Starte die App – ohne diese Zeile würde das Fenster nicht angezeigt
fenster.mainloop()
