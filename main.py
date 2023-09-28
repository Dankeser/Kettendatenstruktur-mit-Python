# Node enthält 3 Methoden:
#   1-value --> zeigt den Wert von sich
#   2-next  --> zeigt nächste
#   3-previous --> zeigt vorherige
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.previous = None

class Chain:
    # neue Chain kommt mit values in List Type
    def __init__(self,values):
        self.instanzlist = []
        self.values = values
        self.list = self._create_chain(self.values)


    # das ermöglicht uns es, dem Objekt ein index zu geben
    def __getitem__(self, item):
        if item > len(self.list)-1:
            print("error")
            return
        else:
            return self.list[item]

    # das ist innere Funktion, die die Liste je nach Kopf oder Fuß von Liste erstellt.
    def _create_chain(self,values):
        l = self.instanzlist
        for x in values:
            l.append(Node(x))
        for index,x in enumerate(values):
            if index == 0:
                l[index].next = l[index+1]
            elif index == len(values) - 1:
                l[index].previous = l[index-1]
            else:
                l[index].next = l[index+1]
                l[index].previous = l[index-1]
        return l

    # diese Funktion macht zuerst die Verbindungden zwischen Vorherige und Nächste, dann
    # löscht index in der Liste.
    def delete(self,index):
        l = self.instanzlist[index]
        if l.previous and l.next is not None:
            l.previous.next = l.next
            l.next.previous = l.previous
            self.instanzlist.pop(index)
        elif l.previous is None:
            l.next.previous = None
            self.instanzlist.pop(index)
        elif l.next is None:
            l.previous.next = None
            self.instanzlist.pop(index)
