import random
#Se pide el tamaño de la matriz con un bucle que solo permite numeros enteros
while True:
    try:
        n = int(input("Ingrese el tamaño de la matriz: "))
    except ValueError:
        print("Ingrese un numero entero.")
    else:
        break
#Se crea una lista con numeros aleatorios sin repetir con un rango del tamaño al cuadrado
lista = random.sample(range(n**2), (n**2))
#Se crea la matriz con los elementos de la lista
matriz = [[(lista.pop()) for i in range(n)] for i in range(n)]
#Se imprime la matriz
print("Matriz:")
for i in matriz:
    for j in i:
        print(f"{j:3d}", end = " ")
    print()
#Se obtiene la diagonal de la matriza en la variable lista
for i in range(n):
    for j in range(n):
        if i == j:
            lista.append(matriz[i][j])
#Se imprime la lista
print("Diagonal de la matriz:\n",lista)
#Se obtiene la otra diagonal de la matriz en la variable lista2
lista2 = []
for i in range(n):
    lista2.append(matriz[i][(n-1)-i])
#Se imprime lista2
print("Diagonal invertida de la matriz:\n",lista2)