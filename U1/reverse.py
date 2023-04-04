# def revertir(lista):
#     i = 0
#     j = (len(lista)) - 1
#     while i < (len(lista) / 2):
#         lista[i], lista[j] = lista[j], lista[i]
#         i += 1
#         j -= 1
#     return lista
# vector = [0,1,2,3,4,5,6,7,8,9,10]
#
# print(revertir(vector))

p = ['lunes','martes','miercoles','jueves','viernes','sabado','domingo']
def fun(i):
    if i == 6:
        return
    fun(i+1)
    print(p[i])


fun(0)