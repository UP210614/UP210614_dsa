
class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
    def getData(self):
        return self.data
    def setData(self,data):
        self.data = data

class Lista:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def isEmpty(self):
        return True if self.size == 0 else False
    def insert(self,dato):
        newNode = Node(dato)
        pos = 0
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        elif dato <= self.head.data:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        else:
            dir = self.head

            # while dir.next != None:
            #     if dato <= dir.data:
            #         newNode.prev = dir.prev
            #         newNode.next = dir
            #         dir.prev.next = newNode
            #         dir.prev = newNode
            #         self.size += 1
            #         return
            #     dir = dir.next
            #     a = dir.data
            while True:
                if dato <= dir.data:
                    newNode.prev = dir.prev
                    newNode.next = dir
                    dir.prev.next = newNode
                    dir.prev = newNode
                    self.size += 1
                    return
                elif dir.next == None:
                    break
                dir = dir.next
            newNode.prev = dir
            dir.next = newNode
            self.tail = newNode
        self.size +=1
    def recorrerDerecha(self):
        lista = []
        dato = self.head
        for i in range(self.size):
            lista.append(dato.data)
            dato = dato.next
        return lista
    def recorrerIzquierda(self):
        lista = []
        dato = self.tail
        for i in range(self.size):
            lista.append(dato.data)
            dato = dato.prev
        return lista

a = Lista()
a.insert(4)
a.insert(3)
a.insert(2)
a.insert(1)
a.insert(5)
a.insert(4.5)
a.insert(6)
a.insert(4)
a.insert(4.6)
a.insert(5.5)

print(a.recorrerDerecha())
print(a.recorrerIzquierda())