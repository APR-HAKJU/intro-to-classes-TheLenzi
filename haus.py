# TODO: Aufgabe 1:
# Ändere den Code unten, so dass die Eigenschaften des Hauses als Attribute im Konstruktor definiert sind.
# Aktuell werden die Eigenschaften als separate Variablen definiert.
# Definiere einen Konstruktor (__init__), um die Attribute zu initialisieren.
class Haus:
    def __init__(self, quadratmeter, schlafzimmer, badezimmer):
        self.quadratmeter = quadratmeter
        self.schlafzimmer = schlafzimmer
        self.badezimmer = badezimmer
    
haus_1 = Haus(quadratmeter = 120, schlafzimmer = 3, badezimmer = 2)


print(f"Haus: {haus_1.quadratmeter}m², {haus_1.schlafzimmer} Schlafzimmer")

# TODO: Aufgabe 2: Erstelle drei weitere Objekte der Klasse Haus mit unterschiedlichen Eigenschaften.


# TODO: Aufgabe 3: Gib die Anzahl der Schlafzimmer und Badezimmer für jedes Haus aus.