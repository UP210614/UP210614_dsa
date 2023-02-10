palabra=input("Dame una palabra: ")
lista=list(palabra)
N=int(len(lista))
for j in range (N):
    if j == len(lista)-1:
        break
    if (lista[j]==' '):
        del(lista[j])
igual=0
print(lista)
for i in range(len(lista)):
    if  lista[i]==lista[(len(lista))-i-1]:
        igual+=1
if igual == int(len(lista)):
    print ("El numero es Palindromo")
else:
    print ("El numero no es Palindromo")