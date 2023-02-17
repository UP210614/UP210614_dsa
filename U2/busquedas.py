def linearNotSort(lista, n):
    for i in range(len(lista)):
        if lista[i] == n:
            return i + 1
    return None
def linearSort(lista, n):
    for i in range(len(lista)):
        if lista[i] > n:
            return None
        if lista[i] == n:
            return i + 1
    return None

lista = [-5,2,3,6,1,9,14]
lista2 = [-3,0,5,7,9,10,14]
numero = int(input("Ingrese un numero: "))
print(linearSort(lista2,numero))




