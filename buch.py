# TODO: 
# Aufgabe 1:
"""Erstelle eine Klasse Buch mit folgenden Attributen:


- titel
- autor
- seiten
- gelesen (Boolean )

Erstelle zwei Bücher: Eines, das du gelesen hast (setze gelesen=True), 
und eines, das du noch nicht gelesen hast.
"""

# TODO: Aufgabe 2:
# Gib für jedes Buch eine Nachricht aus, die angibt, ob du das Buch gelesen hast oder nicht.

class Buch:
    def __init__(self, titel, autor, seiten, gelesen):
        self.titel = titel
        self.autor = autor
        self.seiten = int(seiten)
        self.gelesen = bool(gelesen)

buch_1 = Buch(titel = "Buch1", autor = "Autor1", seiten = "1", gelesen = True)
buch_2 = Buch(titel = "Buch2", autor = "Autor2", seiten = "100", gelesen = False)

print(f"Das Buch {buch_1.titel} wurde {buch_1.gelesen} gelesen")