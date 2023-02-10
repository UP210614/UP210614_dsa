
def prioridad(c):
    if c in ['+','-']:
        return 1
    elif c in ['*','/']:
        return 2
    elif c == '^':
        return 3
    elif c in ['(',')']:
        return 4
p = ['5','6','2','+','*','12','4','/','-',')']
a = [5,6,2,'+','*',12,4,'-','-']
cola = []
i = 0
operacion = True
for i in p:
    try:
        a = float(i)
        cola.append(a)
    except ValueError:
        match (i):
            case '+':
                b = cola.pop()
                a = cola.pop()
                c = a+b
                cola.append(c)
            case '/':
                b = cola.pop()
                a = cola.pop()
                c = a/b
                cola.append(c)
            case '-':
                b = cola.pop()
                a = cola.pop()
                c = a-b
                cola.append(c)
            case '*':
                b = cola.pop()
                a = cola.pop()
                c = a * b
                cola.append(c)
            case ')':
                break
            case _:
                operacion = False
                break
if operacion is True:
    value = cola.pop()
    print(value)
else:
    print("Introduzca una operación válida")

