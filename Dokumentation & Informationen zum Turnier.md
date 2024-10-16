# Maturaarbeit
## Auf der Suche nach möglichst guten Strategien für das Spiel "Monopoly"


#### Ordnerstruktur

```bash
├── Dokumentation & Informationen zum Turnier.md
├── Erklärung der Dokumentation
│   ├── Ergebnis
│   ├── main spieler_2.py
│   ├── spiel_2.py
│   └── spieler_2.py
├── Finale Strategien
│   ├── Ergebnisse
│   ├── main_final.py
│   ├── spiel_final.py
│   ├── strategie_1.py
│   ├── strategie_2.py
│   ├── strategie_3.py
│   ├── strategie_4.py
│   └── strategie_5.py
├── Geldbasierte Strategien des Turniers
│   ├── Ergebnisse_3
│   ├── Ergebnisse3.xlsx
│   ├── main_3.py
│   ├── spiel_3.py
│   └── spieler_3.py
├── M.py
├── Random
│   ├── main_random.py
│   ├── spiel_random_geld.py
│   ├── spiel_random_wahrscheinlichkeiten.py
│   ├── spieler_random.py
│   ├── strategie_1.py
│   ├── strategie_10.py
│   ├── strategie_2.py
│   ├── strategie_3.py
│   ├── strategie_4.py
│   ├── strategie_5.py
│   ├── strategie_6.py
│   ├── strategie_7.py
│   ├── strategie_8.py
│   └── strategie_9.py
├── Wahrscheinlichkeitsbasierte Strategien des Turniers
│   ├── Ergebnisse
│   ├── Ergebnisse4.xlsx
│   ├── main_4.py
│   ├── spiel_4.py
│   └── spieler_4.py
├── bahnen.py
├── grafisch main.py
├── image
│   └── Spielfeld_Monopoly.png
├── immobilie.py
├── spiel.py
├── spieler.py
├── spieler_mensch.py
├── werke.py
└── Übungsprogramm
    ├── Strategie_1
    │   ├── main spieler_1.py
    │   └── spieler_1.py
    └── np.py
```

### Dokumentation des Programms

Die folgenden Programmdateien bilden die Basis für die spezifischen Programme der Strategien. Diese spezifischen Programme unterscheiden sich nicht wesentlich von den Basisprogrammen und sind durch diese Erläuterungen weitgehend selbsterklärend.  Zusätzlich müssen die Module NumPy und Pygame installiert werden.


#### Immobilie.py
##### Attribute:
Die meisten Attribute sind durch ihren Namen selbsterklärend. 
- self.x und self.y sind wichtig für die Position in der grafischen Umsetzung
- self.startwert ist der Kaufpreis des Grundstückes
- self.farbe Immobilien sind auf  Spielfeld in Farbgruppen angeordnet(wichtig für das synchronen Bauen) und hier ist die jeweilige Gruppe gespeichert. 

##### Eigenschaften:
<br>Bauen:<br>
- Überprüft mit der Funktion Bauenüberprüfen(), ob man bauen darf.
- Zieht Geld ab, baut das Haus und steigert den Preis des Feldes.
  
<br>Abbauen:<br>
- Überprüft mit der Funktion Abbauenüberprüfen(), ob man abbauen darf.
- Gibt ein Teil des Geldes zurück, baut Haus ab und senkt den Preis des Feldes.

  
<br>Bauenüberprüfen:<br>
- In den ersten ca. 9 Zeilen überprüft das Programm ob schon alle Häuser, respektive Hotels verbaut wurden.
- Dann kommt für jede Immobiliengruppe («Farbgruppe») ein Teil, der überprüft, ob man bauen kann, da innerhalb der Gruppe synchron gebaut werden muss.

  
<br>Abbauenüberprüfen:<br>
- Überprüft, ob man abbauen darf, da dies auch synchron erfolgen muss (funktioniert genauso wie Bauenüberprüfen()).


#### Bahnen.py und Werke.py
Beide sind eigentlich gleich wie Immobilien.py, mit den Unterschieden, dass man auf ihnen nicht bauen kann und dass die Beträge, die man dem Eigentümer beim Betreten des Feldes zahlen muss, anders berechnet werden. Diese Beträge werden jedoch an einem anderen Ort berechnet (spieler.py). Darum ist diese Klasse sehr ähnlich wie die Immobilienklasse.



#### Spieler.py

##### Attribute:
 Die meisten Attribute sind vom Namen her selbsterklärend
- self.pasch ist eine Angabe wie viel Mal hintereinander ein Pasch geworfen wurde
- self.posx und self.posy sind die Position des Spielers auf dem Spielbrett in der grafischen Umsetzung
- self.gefängniskarten ist die Anzahl der Karten die man besitzt, mit denen man ohne Busse aus dem Gefängnis gehen kann
- self.gekauft ist eine Liste mit allen gekauften Immobilien
- self.bahnen,self.werke,self.eins-self.acht sind Listen mit den entsprechenden Immobilien der jeweiligen Gruppen. Es braucht sie für das Überprüfen des synchronen Bauens.
- self.gefängnis Kann die Werte True oder False haben. Ist zur Überprüfung, ob man nur besuchsweise im Gefängnis oder richtig im Gefängnis ist.
##### Eigenschaften:
Wurf:<br>
1.	Das Programm erstellt zufällig die Ergebnisse der beiden Würfel
2.	Es schaut, ob man ein Pasch geworfen hat.
3.	Es wird kontrolliert, ob es das dritte Pasch in Folge ist. Wenn dies der Fall ist, wird der Spieler ins Gefängnis geschickt.
4.	Ist dies nicht der Fall, so zieht man vorwärts und es überprüft gewisse Sachen, wie zum Beispiel ob ich eine Ereigniskarte ziehen muss, ob ich über den Start gezogen bin und deshalb ein Rundenkapital erhalte oder ob ich wegen des Polizistenfelds ins Gefängnis gehen muss.
5.	Als nächstes wird die bezahl und die kauf Funktion aufgerufen.
6.	Wenn ich in diesem Wurf einen Pasch geworfen habe und alle erlaubten Aktionen durchgeführt wurden, muss ich die Funktion Wurf() erneut durchlaufen.
7.	Als letztes werde ich, wenn ich im Gefängnis bin, noch bestraft. Dies entweder mit einer Busse oder so dass ich eine Gefängniskarte verliere.

Bezahlen:<br>
Zuerst sucht man, ob die eigene Position mit der eines verkauften Grundstückes übereinstimmt. Dann wird überprüft, ob es sich um ein Werk, eine Bahn oder um eine normale Immobilie handelt. Als letztes wird dem Besitzer die entsprechende Summe bezahlt, ist die Immobilie ein Werk oder eine Bahn muss diese Summe zuerst noch ermittelt werden.

Kaufen:<br>
Diese Funktion wird aufgerufen, wenn man ein Grundstück kaufen will. Zuerst wird überprüft, ob das Feld schon verkauft wurde oder nicht. Ist es noch nicht verkauft, wird es wieder nach Farbgruppe gruppiert. In den Gruppen wird es in die entsprechende Liste hinzugefügt und wenn man dann die Gruppe komplett hat, wird der Anfangswert verdoppelt. Als letztes zahlt man noch den Kaufpreis und gewisse Listen werden aktualisiert.

Kanzlei und Chance:<br>
Bei beiden Ereigniskarten läuft es gleich ab. Als erstes wird überprüft, ob man den Stapel der Karten neu auffüllen müssen. Danach wird mit einer Zufallszahl eine zufällige Karte gezogen und die entsprechende Aktion wird ausgeführt. Am Ende wird diese Karte aus dem Stapel entfernt.

Grafische Position:<br>
Rechnet die Position des Spielers in der grafischen Umsetzung aus.

Wurf_grafisch:<br>
Macht das Gleiche wie die Funktion «Wurf», ausserdem sind hier noch die Funktionen draw() und grafischeposition() integriert. Diese sind zuständig, dass der Spieler auch während seinem Zug auf dem grafischen Spielfeld gezeichnet wird.

#### M.py
Hier wird zuerst die Matrix definiert. In der Funktion Wahrscheinlichkeiten() wird die Zugwahrscheinlichkeit nach einer bestimmten Anzahl von Zügen ausgerechnet. Die Matrix findet sich auch noch in einer Excel-Datei wieder.

#### Np.py

In diesem Programm habe ich mir das Rechnen mit Matrizen am Computer beigebracht. Hier findet man noch eine Funktion für Eigenwerte und Eigenvektoren, die ich in M.py nie verwendet habe. 


#### Spiel.py
In der Funktion Spiel wird zuerst alles nötige importiert und initialisiert, wie zum Beispiel die Immobilien oder die Ereigniskartenliste.
In der for-Schleife findet dann erst das richtige Spiel statt.
1.	Es wird die Funktion Wurf aufgerufen.
2.	In einer for-Schleife werden die gekauften Immobilien durchlaufen, und es kann gebaut werden.
3.	Wenn man im Minus ist, so werden, solange man noch Häuser hat, Häuser in einer «while True Schleife» abgebaut. Kommt man nicht aus dem Minus, so wird die Funktion mit einem return beendet, welche den Sieger in Form einer Zahl zurückgibt.
4.	Der zweite Spieler ist an der Reihe.
5.	Ist das Spiel nach 10000 Zügen nicht beendet, so wird der Spieler mit mehr Geld zum Sieger.



#### Grafisch Main.py

Funktioniert gleich wie das Programm Spiel, hat den Unterschied das die grafischen Elemente noch in das Programm mit einfliessen.  Es ist ein Programm in dem einen Spieler das Spiel gegen die Siegerstrategie spielen kann.  Wenn man es startet, öffnet sich ein Fenster mit dem Spiel. Die Aktionen werden jedoch durch Eingaben (die Eingaben sind Buchstaben, die zusammen mit den dazugehörigen Aktionen angezeigt werden) im Terminal/Inputfeld gesteuert. Um das Spiel zu starten, drückt der Spieler die Leertaste, sobald das Monopoly-Fenster geöffnet ist. "spieler_mensch.py" ist die "spieler.py" Version für den menschlichen Spieler.

## Das Implementieren einer Strategie am Beispiel aus dem Ordner "Erklärung der Dokumentation":

Wir haben das Auswertungsprogramm «main spieler_2.py».
In das importieren wir eine neue erstellte Version der Programme Spiel.py und Spieler.py, welche auf die spezifischen Strategien zugeschnitten sind. Hier sind das «spiel_2.py» und «spieler_2.py» welches einfach Kopien mit kleinen Änderungen der originalen «spieler.py» und «spiel.py» sind.
In der Auswertung erstellet man für jeden Parameter eine Liste, in welche man die entsprechenden Werte einfüllt (z.B. werte1=[0.2,0.4,0.6,0.8,1]). Danach passt man die Auswertungsliste an die Anzahl und Länge der Parameterlisten an.
Danach fügt man in der init Funktion des Spielers die Parameter hinzu. In diesem Beispiel wird nur ein Wert pro Entscheidungssituation übergeben. Als nächstes modifiziert man die  neuen Programme «spieler_2.py» und «spiel_2.py», so dass  diese Werte an den Spieler übergeben werden und diese an den richtigen Stellen die Entscheidungen bestimmen.
Jetzt passt man den Block mit den for-Schleifen an. Es muss für den ersten Spieler für jeden Parameter eine Schleife geben, dasselbe dann auch noch für den zweiten Spieler.
Am Ende muss man im Teil unter den for-Schleifen die Initialisierung der Spieler, den Vergleich ob zweimal dieselbe Strategie vorhanden ist und die Addition in der Auswertungsliste an die Anzahl der Parameter, anpassen.
Für die Strategien des Turniers wurden auch immer leicht angepasste Versionen der Programme erstellt.

## Das Turnier

### Runde 1

Alle geldbasierten Strategien und deren Ergebnisse befinden sich im Ordner "Geldbasierte Strategien des Turniers".
Alle wahrscheinlichkeitsbasierten Strategien und deren Ergebnisse befinden sich im Ordner "Wahrscheinlichkeitsbasierte Strategien des Turniers".

### Runde 2

Die Programme zu dieser Runde befinden sich im Ordner "Random".

Die fünf besten geldbasierten Strategien sind in der Reihenfolge der Rangliste als Strategien 1-5 in dem Ordner.
Die fünf besten wahrscheinlichkeitsbasierten Strategien sind in der Reihenfolge der Rangliste als Strategien 6-10 in dem Ordner.

### Runde 3

Im Ordner "Finale Strategien" befinden sich alles aus Runde 3.

