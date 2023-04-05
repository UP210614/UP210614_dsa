
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
            self.size +=1
            return pos
        elif dato <= self.head.data:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            self.size +=1
            return pos
        else:
            dir = self.head
            pos = 0
            while dir.next is not None and dir.next.data <= dato:
                dir = dir.next
                pos += 1
            newNode.prev = dir
            newNode.next = dir.next
            if dir.next is not None:
                dir.next.prev = newNode
            else:
                self.tail = newNode
            dir.next = newNode
            self.size += 1
            pos += 1
            return pos

    def recorrerDerecha(self):
        dato = self.head
        lista = ""
        for i in range(self.size):
            if i < self.size - 1:
                lista += str(dato.data) + " --> "
            else:
                lista += str(dato.data)
            dato = dato.next
        return lista
    def recorrerIzquierda(self):
        dato = self.tail
        lista = ""
        for i in range(self.size):
            if i < self.size - 1:
                lista += str(dato.data) + " --> "
            else:
                lista += str(dato.data)
            dato = dato.prev
        return lista
    def seek(self,pos):
        if pos < self.size and self.isEmpty() is False and pos >= 0:
            dir = self.head
            for i in range(pos):
                dir = dir.next
            return dir.data
        else:
            return None
    def search(self,value):
        if self.isEmpty() is False:
            dir = self.head
            for i in range(self.size):
                if dir.data == value:
                    return i
                dir = dir.next
            return None
        else:
            return None
    def removePosition(self,pos):
        if pos < self.size and self.isEmpty() is False:
            dir = self.head
            if pos == 0:
                eliminar = dir
                dato = dir.data
                dir.next.prev = None
                self.head = dir.next
                self.size-=1
                del eliminar
                return dato
            else:
                for i in range(pos):
                    dir = dir.next
                eliminar = dir
                dato = dir.data
                if dir.next != None:
                    dir.prev.next = dir.next
                    dir.next.prev = dir.prev
                else:
                    dir.prev.next = None
                    self.tail = dir.prev
                del eliminar
                self.size-=1
                return dato
        else:
            return None
    def removeValue(self,value):
        if self.isEmpty() is False:
            dir = self.head
            if value == self.head.data:
                eliminar = dir
                dato = dir.data
                dir.next.prev = None
                self.head = dir.next
                self.size -= 1
                del eliminar
                return dato
            else:
                while value != dir.data:
                    dir = dir.next
                eliminar = dir
                dato = dir.data
                if dir.next != None:
                    dir.prev.next = dir.next
                    dir.next.prev = dir.prev
                else:
                    dir.prev.next = None
                    self.tail = dir.prev
                del eliminar
                self.size -= 1
                return dato
        else:
            return None

