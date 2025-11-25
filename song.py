# Gegeben ist eine Liste, die Informationen über verschiedene Songs enthält.
# Verändere den Code so, dass eine Klasse "Song" definiert wird.
# Die Eigenschaften Titel, Künstler und Anzahl der Streams sollen als Attribute im Konstruktor definiert werden


#TODO: Aufgabe 1: 
#   Definiere die Klasse "Song" mit einem Konstruktor (__init__),
#  der die Attribute titel, künstler und streams initialisiert.

# TODO: Aufgabe 2:
#   Erstelle drei Objekte der Klasse "Song" mit den Informationen aus der Liste oben

# TODO: Aufgabe 3:
#   Gib für jeden Song den Titel und die Anzahl der Streams in folgendem Format aus:
#   "Der Song '<Titel>' von <Künstler> hat <Anzahl der Streams> Streams."

class Song:
    def __init__(self, titel, künstler, streams):
        self.titel = titel
        self.künstler = künstler
        self.streams = int(streams)

song_1 = Song(titel="Blinding Lights", künstler = "The Weeknd", streams = 4_200_000_000)
song_2 = Song(titel= "Shape of You", künstler="Ed Sheeran", streams= 5_300_000_000) 
song_3 = Song(titel="Dance Monkey", künstler="Tones and I", streams=3_400_000_000)


print(f"Der song {song_1.titel} von {song_1.künstler} hat {song_1.streams} Streams")
print(f"Der song {song_2.titel} von {song_2.künstler} hat {song_2.streams} Streams")
print(f"Der song {song_3.titel} von {song_3.künstler} hat {song_3.streams} Streams")