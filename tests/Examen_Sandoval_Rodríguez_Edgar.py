
def recorrerDerecha(lista,numero):
    for i in range(numero):
        lista.insert(0, lista.pop())
    return lista

# lista = [5,2,1,6,3,4,7,9]
#
# c = int(input("Ingresa un numero: "))
#
# print(recorrerDerecha(lista,c))

def estaBalanceado(operación):
    stack = []
    for i in operación:
        if i == '(':
            stack.append(i)
        elif i == ')' and '(' in stack:
            stack.pop()
    return not (bool(stack))

lista2 = ['(())()','(()',')()(','(a*+())b()','())(','']

for i in lista2:
    resultado = estaBalanceado(i)
    print(f"'{i}' ¿Está balanceado? {resultado}")





