
def prioridad(c):
    if c in ['+','-']:
        return 1
    elif c in ['*','/']:
        return 2
    elif c == '^':
        return 3
    elif c in ['(',')']:
        return 4

p = "2+5+6 *(1+2)"
p.split()
for i in p:
    try:
        float(i)
        print(f"{i} Es un operando")
    except ValueError:
        if i in ['+','-','/','*','(',')','^']:
            print(f"{i} Es un operador con prioridad {prioridad(i)}.")
        else:
            print(f"{i} Es un carácter")

