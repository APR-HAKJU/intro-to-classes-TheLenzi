"""
Übung 3: Einkaufswagen

Aufgabe:
Erstelle zwei Klassen:
1. Artikel: Repräsentiert einen einzelnen Artikel mit Name und Preis
2. Einkaufswagen: Verwaltet eine Liste von Artikel-Objekten

Der Einkaufswagen soll:
- Artikel hinzufügen können
- Den Gesamtpreis berechnen
- Die Anzahl der Artikel zählen
- Den Inhalt anzeigen
"""

# TODO 1: Erstelle die Klasse Artikel mit passendem Konstruktor
class Artikel:
    def __init__(self,Name,Preis):
        self.Name = Name
        self.Preis = float(Preis)

    def zeige_info(self):
        print(f"{self.Name}: {self.Preis} EUR")


neuerartikel = Artikel(Name="PS5 Controller", Preis=79.99 )


# TODO 2: Erstelle die Klasse Einkaufswagen
class Einkaufswagen:
    def __init__(self):
        self.artikel = []

    """
    Ein Einkaufswagen der Artikel-Objekte verwaltet.
    
    Attribute:
    - artikel (list): Liste von Artikel-Objekten
    """
    
    # TODO 2.1: Schreibe den Konstruktor __init__
    # Keine Parameter außer self
    # Initialisiere eine leere Liste self.artikel = []
    pass
    
    # TODO 2.2: Schreibe die Methode hinzufuegen(artikel)
    # Parameter: self, artikel (ein Artikel-Objekt)
    # Füge das Artikel-Objekt zur Liste hinzu
    # Gib aus: "✅ {artikel.name} hinzugefügt"
    pass

    def hinzufuegen(self,artikel):
        self.artikel.append(artikel)
        print(f"{artikel.Name} hinzugefügt")


    
    # TODO 2.3: Schreibe die Methode gesamtpreis()
    # Keine Parameter außer self
    # Berechne die Summe aller Preise (artikel.preis)
    # Gib die Summe zurück (return)
    
    def gesamtpreis(self):
        summe = 0
        for a in self.artikel:
            summe = summe + a.preis
        return summe
    
    # TODO 2.4: Schreibe die Methode anzahl_artikel()
    # Keine Parameter außer self
    # Gib die Anzahl der Artikel zurück (len(self.artikel))
    
    def anzahl_artikel(self):
        return len((self.artikel))
    
    # TODO 2.5: Schreibe die Methode zeige_inhalt()
    # Keine Parameter außer self
    # Gib aus: "Einkaufswagen ({anzahl} Artikel):"
    # Für jeden Artikel: Rufe artikel.zeige_info() auf
    # Gib aus: "Gesamtpreis: {gesamtpreis} EUR"
    
    def zeige_inhalt(self):
        print(f"Anzah der Artikel {self.anzahl_artikel()}")

        for a in self.artikel:
            a.zeige_info()
        
        print(f"Gesamtsumme {self.gesamtpreis()}")

# TODO 3.1: Erstelle drei Artikel-Objekte
# artikel1 = Artikel("Brot", 2.99)
# artikel2 = Artikel("Milch", 1.49)
# artikel3 = Artikel("Käse", 4.50)

wagen = Einkaufswagen()


artikel1 = Artikel("Brot", 2.99)
artikel2 = Artikel("Milch", 1.49)
artikel3 = Artikel("Käse", 4.50)

# TODO 3.2: Erstelle einen Einkaufswagen
# wagen = Einkaufswagen()


# TODO 3.3: Füge die drei Artikel zum Wagen hinzu
wagen.hinzufuegen(artikel1)
wagen.hinzufuegen(artikel2)
wagen.hinzufuegen(artikel3)

print(wagen.anzahl_artikel())



# TODO 3.4: Zeige den Inhalt des Wagens
# wagen.zeige_inhalt()
pass


"""
Erwartetes Ergebnis:
✅ Brot hinzugefügt
✅ Milch hinzugefügt
✅ Käse hinzugefügt

Einkaufswagen (3 Artikel):
- Brot: 2.99 EUR
- Milch: 1.49 EUR
- Käse: 4.50 EUR
Gesamtpreis: 8.98 EUR
"""
