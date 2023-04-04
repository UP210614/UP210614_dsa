
def binarySearch(lista,value):
    prin= 0
    final = len(lista)
    mit = (prin+final)//2
    c = 0
    while prin <= final and lista[mit] != value:

        if value<lista[mit]:
            final = mit-1
        else:
            prin= mit+1
        mit = (prin+final)//2
        c += 1
    if lista[mit] == value:
        return mit,c
    else:
        return None,c




lista= [-3,0,1,5,7,9]
n = int(input("Ingresa un numero: "))
print(binarySearch(lista,n))