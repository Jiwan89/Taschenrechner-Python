def rechner():
    zahl1 = float(input("Gib die erste Zahl ein: "))
    operator = input("Operator wählen (+, -, *, /): ")
    zahl2 = float(input("Gib die zweite Zahl ein: "))

    if operator == "+":
        ergebnis = zahl1 + zahl2
    elif operator == "-":
        ergebnis = zahl1 - zahl2
    elif operator == "*":
        ergebnis = zahl1 * zahl2
    elif operator == "/":
        if zahl2 != 0:
            ergebnis = zahl1 / zahl2
        else:
            print("Fehler: Division durch 0 ist nicht erlaubt.")
            return
    else:
        print("Ungültiger Operator!")
        return

    print("Ergebnis:", ergebnis)

rechner()
