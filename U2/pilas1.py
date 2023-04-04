def revertir(lista):
    i = 0
    j = (len(lista)) - 1
    while i < (len(lista) / 2):
        lista[i], lista[j] = lista[j], lista[i]
        i += 1
        j -= 1
    return lista

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def setData(self, dato):
        self.data = dato

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def getSize(self):
        return self.size

    def isEmpty(self):
        return True if self.size == 0 else False

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        self.size += 1

    def pop(self):
        dato = None
        if self.isEmpty() is False:
            dato = self.head.data
            self.head = self.head.next
            self.size -= 1
            return dato
        return 'La lista está vacia'

    def show(self):
        if self.isEmpty() is False:
            dir = self.head
            componentes = []
            for i in range(self.size):
                componentes.append(dir.data)
                dir = dir.next
            componentes = revertir(componentes)
            return componentes
        else:
            return "La lista está vacia"
    def peek(self):
        if self.isEmpty() is False:
            a = self.head.data
            return a
        return "La lista está vacia"
    def existe(self,dato):
        if self.isEmpty() is False:
            dir = self.head

            for i in range(self.size):
                if dato == dir.data:
                    return True
                dir = dir.next
            return False
        else:
            return "La lista está vacia"

class Queu:
    def __init__(self):
        self.head = None
        self.size = 0
        self.tail = None
    def getSize(self):
        return self.size
    def isEmpty(self):
        return True if self.head == None and self.tail == None else False


a = Stack()
a.push('Edgar')
a.push('Juan')
a.push('Manuel')
print(a.size)
print(a.peek())
print(a.show())
a.pop()
print(a.show())
a.push("hola")
print(a.show())
print(a.peek())
print(a.existe('dsfsd'))
b = Queu()

print(b.isEmpty())