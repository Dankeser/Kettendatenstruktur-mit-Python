instanzlist = []

# Node enthält 3 Methoden:
#   1-value --> zeigt den Wert von sich
#   2-next  --> zeigt nächste
#   3-previous --> zeigt vorherige
#   4-delete() --> löschen
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.previous = None

    # diese Funktion macht zuerst die Verbindungden zwischen Vorherige und Nächste, dann
    # löscht sich in der Liste.
    def delete(self):
        if self.previous and self.next is not None:
            self.previous.next = self.next
            self.next.previous = self.previous
            instanzlist.remove(self)
        elif self.previous is None:
            self.next.previous = None

            instanzlist.remove(self)
        elif self.next is None:
            self.previous.next = None
            instanzlist.remove(self)

class Chain:
    # neue Chain kommt mit values in List Type
    def __init__(self,values):
        self.values = values
        self.list = self._create_chain(self.values)
    
    # das ermöglicht uns es, dem Objekt ein index zu geben
    def __getitem__(self, item):
        if item > len(self.list)-1:
            print("error")
            return
        else:
            return self.list[item]
        
    # das ist die innere Funktion, die die Liste je nach Kopf oder Fuß von Liste erstellt.
    def _create_chain(self,values):
        for x in values:
            instanzlist.append(Node(x))
        for index,x in enumerate(values):
            if index == 0:
                instanzlist[index].next = instanzlist[index+1]
            elif index == len(values) - 1:
                instanzlist[index].previous = instanzlist[index-1]
            else:
                instanzlist[index].next = instanzlist[index+1]
                instanzlist[index].previous = instanzlist[index-1]
        return instanzlist
