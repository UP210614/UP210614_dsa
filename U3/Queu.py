class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def getData(self):
        return self.data
    def setData(self,data):
        self.data = data

class Queu:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def getSize(self):
        return self.size
    def isEmpty(self):
        return True if not self.head else False
    def enque(self,dato):
        newNode = Node(dato)

        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1
    def deque(self):
        dato = None
        if self.isEmpty() is False:
            dato = self.head.data
            self.head = self.head.next
            self.size -=1
            return dato
        else:
            return "La lista está vacía"
    def show(self):
        lista = []
        dato = self.head
        if self.isEmpty() is False:
            for i in range(self.size):
                lista.append(dato.data)
                dato = dato.next
            return lista
        else:
            return lista
    def existe(self,dato):
        dir = self.head
        for i in range(self.size):
            if dato == dir.data:
                return True
            dir = dir.next
cola = Queu()
cola.enque(5)
cola.enque(7)
cola.enque(8)
cola.enque(6)
print(cola.head.data)
print(cola.tail.data)
print(cola.show())




