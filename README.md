# Kettendatenstruktur-mit-Python
Ein Versuch für Kettendatenstruktur in Python,

Kettendatenstruktur ist ein Datenstruktur wie eine Kette, indem jede Teile von Kette sich die Nachbarn merken.
Um ein neue Kette zu erstellen, geben wir eine liste in Chain Klasse ein und speichern es in einer Variable.
Dann können wir mit İndexnummer die Nachbarn erhalten, indem wir **.value**, **.next**, **.previous** Attribute benutzen.
Beispiel:


![image](https://github.com/Dankeser/Kettendatenstruktur-mit-Python/assets/131388485/297c2a69-d38a-4a87-880c-311d17f5f91d)


Zusätzlich hat Node Klasse .delete Attribute, was den Teil der Kette löscht.
Beispiel:
'''
newchain[2].delete()
'''
