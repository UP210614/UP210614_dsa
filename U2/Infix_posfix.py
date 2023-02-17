
def prioridad(c):
    if c in ['+','-']:
        return 1
    elif c in ['*','/']:
        return 2
    elif c == '^':
        return 3
    elif c in ['(',')']:
        return 0

n = ["5","*","(","6","+","2",")","-","12","/","4"]
n.append(')')
n.insert(0,'(')

def infix_posfix(n):
    p = []
    stack = []

    for i in n:
        if i not in ['+','-','/','*','(',')']:
            p.append(i)
        elif i == '(':
            stack.append(i)
        elif i in ['+', '-', '/', '*']:
            contador = len(stack)-1
            while prioridad(stack[contador]) >= prioridad(i):
                    p.append(stack.pop())
                    contador-=1
            stack.append(i)
        elif i == ')':
            contador = len(stack) - 1
            while stack[contador] != '(':
                p.append(stack.pop())
                contador-=1
            stack.pop()
    p.append(')')
    return p

print(infix_posfix(n))