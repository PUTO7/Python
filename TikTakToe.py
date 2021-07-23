# Wilkommensnachricht
print("Tic-Tac-Toe Python")


# Spielfeld ausgeben
def spielfeld_ausgeben(spielfeld):
    print("+++++++++++\n+         +")
    for line in (spielfeld[1:4], spielfeld[4:7], spielfeld[7:]):
        print(f"+  {'|'.join(line)}  +")
    print("+         +\n+++++++++++")


# Die Spieler Eingabe
def spieler_eingabe(versuche, spielfeld, spieler_aktuell):
    print("Spieler am Zug", spieler_aktuell)
    zug_gemacht = False
    while not zug_gemacht:
        spieler_zug = int(input("Auf welches Feld setzt du? "))
        if spielfeld[spieler_zug].isnumeric():
            spielfeld[spieler_zug] = spieler_aktuell
            zug_gemacht = True
        else:
            print("Da hat Spieler",
                  spielfeld[spieler_zug], "schon einen zug gemacht.")


# Kontrolle ob und wer das Spiel gewonnen hat.
def kontrolle_gewonnen(versuche, spielfeld, spieler_aktuell):
    if (spielfeld[1] == spielfeld[2] == spielfeld[3]
        or spielfeld[4] == spielfeld[5] == spielfeld[6]
        or spielfeld[7] == spielfeld[8] == spielfeld[9]
        # Kontrolle auf Spalten
        or spielfeld[1] == spielfeld[4] == spielfeld[7]
        or spielfeld[2] == spielfeld[5] == spielfeld[8]
        or spielfeld[3] == spielfeld[6] == spielfeld[9]
        # Kontrolle auf Diagonalen
        or spielfeld[7] == spielfeld[5] == spielfeld[3]
            or spielfeld[9] == spielfeld[5] == spielfeld[1]):
        print("Du hast das Spiel gewonnen", spieler_aktuell)
        return True
    return False


# Kontrolle ob unentschieden
def kontrolle_auf_unentschieden(versuche):
    if versuche == 9:
        print("Unentschieden! ")
        return True
    return False


# Den aktiven Spieler wechseln X/O
def spieler_change(spieler_aktuell):
    if spieler_aktuell == "X":
        spieler_aktuell = "O"
    else:
        spieler_aktuell = 'X'
    return spieler_aktuell


def main(spielfeld=[" ", "1", "2", "3", "4", "5", "6", "7", "8", "9"], spieler_aktuell="X"):
    versuche = sum([1 if f in "XO" else 0 for f in spielfeld[1:]])

    spielfeld_ausgeben(spielfeld)
    while True:
        spieler_eingabe(versuche, spielfeld, spieler_aktuell)
        if kontrolle_auf_unentschieden(versuche) or kontrolle_gewonnen(versuche, spielfeld, spieler_aktuell):
            erneut_spielen = input("Willst du erneut spielen (y/n)? ")
            if erneut_spielen == "n":
                print("Danke fÃ¼rs Spielen")
                exit()

            spielfeld = [" ", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            spieler_aktuell = "X"
            versuche = 0

        spielfeld_ausgeben(spielfeld)
        spieler_aktuell = spieler_change(spieler_aktuell)
        versuche += 1


if __name__ == "__main__":
    # Spielfeld
    main()