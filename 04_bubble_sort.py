import random

lista = random.sample(range(100),10)
print(lista)

for i in lista:
    for j in range((len(lista))-1):
        if lista[j] > lista[j+1]:
            lista[j],lista[j+1] = lista[j+1],lista[j]
print(lista)