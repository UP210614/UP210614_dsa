import math
operadores = ['+', '-', '/', '*', '(', ')', '^','sen','tan','cos','asin','acos','atan','ln','log']
funciones = ['sen','tan','cos','asen','acos','atan','ln','log']
def prioridad(c):
    if c in ['+','-']:
        return 1
    elif c in ['*','/']:
        return 2
    elif c == '^':
        return 3
    elif c in funciones:
        return 4
    elif c in ['(',')']:
        return 0
def infix_posfix(n):
    n.append(')')
    n.insert(0, '(')
    p = []
    stack = []
    for i in n:
        if i not in ['+', '-', '/', '*', '(', ')', '^','sen','tan','cos','asen','acos','atan','ln','log']:
            p.append(i)
        elif i == '(':
            stack.append(i)
        elif i in ['+', '-', '/', '*','^','sen','tan','cos','asen','acos','atan','ln','log']:
            contador = len(stack)-1
            while prioridad(stack[contador]) >= prioridad(i):
                p.append(stack.pop())
                contador -= 1
            stack.append(i)
        elif i == ')':
            contador = len(stack) - 1
            while stack[contador] != '(':
                p.append(stack.pop())
                contador -= 1
            stack.pop()
    p.append(')')
    return p
def operacion(operacion):
    # if operacion[1] in ['+','-']:
    #     a = operacion[1]+operacion[0]
    #     operacion[0] = a
    #     del operacion[1]
    stack = []
    for i in operacion:
        if i not in ['+','/','-','*','^',')','^','sen','tan','cos','asen','acos','atan','ln','log']:
            numero = float(i)
            stack.append(numero)
        else:
            match (i):
                case '+':
                    b = stack.pop()
                    a = stack.pop()
                    c = a+b
                    stack.append(c)
                case '/':
                    b = stack.pop()
                    a = stack.pop()
                    c = a/b
                    stack.append(c)
                case '-':
                    b = stack.pop()
                    a = stack.pop()
                    c = a-b
                    stack.append(c)
                case '*':
                    b = stack.pop()
                    a = stack.pop()
                    c = a * b
                    stack.append(c)
                case '^':
                    b = stack.pop()
                    a = stack.pop()
                    c = a**b
                    stack.append(c)
                case 'sen':
                    x = math.sin(math.radians(stack.pop()))
                    stack.append(x)
                case 'cos':
                    x = math.cos(math.radians(stack.pop()))
                    stack.append(x)
                case 'tan':
                    x = math.tan(math.radians(stack.pop()))
                    stack.append(x)
                case 'asen':
                    x = math.degrees(math.asin(stack.pop()))
                    stack.append(x)
                case 'acos':
                    x = math.degrees(math.acos(stack.pop()))
                    stack.append(x)
                case 'atan':
                    x = math.degrees(math.atan(stack.pop()))
                    stack.append(x)
                case 'ln':
                    x = stack.pop()
                    stack.append(math.log(x))
                case 'log':
                    x = stack.pop()
                    z = stack.pop()
                    stack.append(math.log(x,z))
                case ')':
                    break
                case _:
                    break
    value = stack.pop()
    return value
def enlistar(n):
    op=[]
    a =''
    for i in n:
        if i not in ['+','-','/','*','(',')','^']:
            a +=i
        else:
            if a!='':
                op.append(a)
            op.append(i)
            a = ''
    if a != '':
        op.append(a)

    return op
def operacionFinal(op):
    a = enlistar(op)
    b = infix_posfix(a)
    c = operacion(b)
    return c

n = input("Introduzca una operación: ")

print(operacionFinal(n))

