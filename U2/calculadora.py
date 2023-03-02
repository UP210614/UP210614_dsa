from collections import deque
def prioridad(c):
    if c in ['+','-']:
        return 1
    elif c in ['*','/']:
        return 2
    elif c == '^':
        return 3
    elif c in ['(',')']:
        return 0
def infix_posfix(n):
    n.append(')')
    n.insert(0, '(')
    p = []
    stack = []
    for i in n:
        if i not in ['+', '-', '/', '*', '(', ')', '^']:
            p.append(i)
        elif i == '(':
            stack.append(i)
        elif i in ['+', '-', '/', '*','^']:
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
    stack = []
    for i in operacion:
        if i not in ['+','/','-','*','^',')','^']:
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
    return op
def operacionFinal(op):
    a = enlistar(op)
    b = infix_posfix(a)
    c = operacion(b)
    return c

n = input("Introduzca una operación: ")

#a = enlistar(n)
#b = infix_posfix(a)
#c = operacion(b)
print(operacionFinal(n))


