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
def enlistar(op):
    op = list(op)
    op.append('a')
    op2 = []
    stack = deque()
    for i in op:

        if i not in ['+','-','/','*','(',')','a','^']:
            stack.append(i)
        elif i in ['+','-','/','*','(',')','a','^']:
            contador = len(stack)-1
            a= ''
            while contador >= 0:
                a = a + stack.popleft()
                contador -= 1
            if a != '':
                op2.append(a)
            if i != 'a':
             op2.append(i)
    return op2
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
print(enlistar(n))


