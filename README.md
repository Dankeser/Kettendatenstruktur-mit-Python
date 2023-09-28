# Ein Versuch für Kettendatenstruktur :chains: in Python,

Kettendatenstruktur ist ein Datenstruktur wie eine Kette, indem jede Teile von Kette sich die Nachbarn merken.
Um ein neue Kette zu erstellen, geben wir eine liste in Chain Klasse ein und speichern es in einer Variable.
Dann können wir mit İndexnummer die Nachbarn erhalten, indem wir **.value**, **.next**, **.previous** Attribute benutzen.
### Beispiel:
```
newchain = Chain(["Erste","Egal ob Nummer ist",3])
print(newchain[0]) # das zeigt das erste element
print(newchain[0].next) # das zeigt das zweiteste element
print(newchain[0].next.value) # das zeigt den wert vom zweitesten element
```
### Ergebnis:
```
<__main__.Node object at 0x00000278CD2856D0>
<__main__.Node object at 0x00000278CD285710>
Egal ob Nummer ist
```
Zusätzlich hat Chain Klasse .delete Attribute, was den Teil der Kette löscht:
```
newchain.delete(2) # das löscht das zweite
```
