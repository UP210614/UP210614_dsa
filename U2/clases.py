class Node:
    def __init__(self,data):
        self.data= data
        self.next = None
    def getData(self):
        return self.data
    def setData(self,dato):
        self.data = dato

nodo1 = Node('El webos')
nodo2 = Node('El nata')
nodo3 = Node("El samu")
nodo1.next = nodo2
nodo2.next = nodo3
print(nodo1.data)
print(nodo1.next.data)
print(nodo1.next.next.data)