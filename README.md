# Kettendatenstruktur-mit-Python
Ein Versuch für Kettendatenstruktur in Python,

Kettendatenstruktur ist ein Datenstruktur wie eine Kette, indem jede Teile von Kette sich die Nachbarn merken.
Um ein neue Kette zu erstellen, geben wir eine liste in Chain Klasse ein und speichern es in einer Variable.
Dann können wir mit İndexnummer die Nachbarn erhalten, indem wir .value, .next, .previous Attribute benutzen.
Beispiel:
    newchain = Chain(["Erste","Egal ob Nummer ist",3])
    print(newchain[0]) # das zeigt das erste element
    print(newchain[0].next) # das zeigt das zweite element
  
