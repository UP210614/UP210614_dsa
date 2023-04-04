from tkinter import *
import math
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
    try:
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
    except:
        return "Syntax Error"
    else:
        return value
def operacionFinal(op):
    a = op.split()
    print(a)
    b = infix_posfix(a)
    print(b)
    c = operacion(b)
    return c
i = 0
a = ''
def click(valor):
    global i
    global a
    display.insert(i,valor)
    a = a + valor
    i+=1
def fun(valor,valor2):
    global i
    global a
    display.insert(i,valor)
    a = a + (' '+valor+' ')
    i+=valor2
def AC():
    global i,a
    display.delete(0,END)
    a = ''
    i = 0
def igual():
    global i
    r = operacionFinal(a)
    AC()
    display.insert(i,r)
def Resta(valor):
    global i
    global a
    display.insert(i,valor)
    a = a + valor
    i+=1

root = Tk()
root.title("Calculadora")
display = Entry(root,font="Calibri 30")
display.grid(row=0,columnspan=5,sticky=W+E,padx=5,pady=5)

botonSen = Button(root, text="sen",font="Calibri",width=5,command= lambda: fun('sen',3)).grid(row=1,column=0,padx=5,pady=5)
botonCos = Button(root, text="cos",font="Calibri",width=5,command= lambda: fun('cos',3)).grid(row=1,column=1,padx=5,pady=5)
botonTan = Button(root, text="tan",font="Calibri",width=5,command= lambda: fun("tan",3)).grid(row=1,column=2,padx=5,pady=5)
botonLn = Button(root, text="ln",font="Calibri",width=5,command= lambda: fun('ln',2)).grid(row=1,column=3,padx=5,pady=5)
botonLog = Button(root, text="log",font="Calibri",width=5,command= lambda: fun('log',3)).grid(row=1,column=4,padx=5,pady=5)

botonAsen = Button(root, text="asen",font="Calibri",width=5,command= lambda: fun('asen',4)).grid(row=2,column=0,padx=5,pady=5)
botonAcos = Button(root, text="acos",font="Calibri",width=5,command= lambda: fun('acos',4)).grid(row=2,column=1,padx=5,pady=5)
botonAtan = Button(root, text="atan",font="Calibri",width=5,command= lambda: fun('atan',4)).grid(row=2,column=2,padx=5,pady=5)
botonParA = Button(root, text="(",font="Calibri",width=5,command= lambda: fun('(',1)).grid(row=2,column=3,padx=5,pady=5)
botonParC = Button(root, text=")",font="Calibri",width=5,command= lambda: fun(')',1)).grid(row=2,column=4,padx=5,pady=5)

boton9 = Button(root,text="9",font="Calibri",width=5,command= lambda: click('9')).grid(row=3,column=2,padx=5,pady=5)
boton8 = Button(root,text="8",font="Calibri",width=5,command= lambda: click('8')).grid(row=3,column=1,padx=5,pady=5)
boton7 = Button(root,text="7",font="Calibri",width=5,command= lambda: click('7')).grid(row=3,column=0,padx=5,pady=5)
botonAC = Button(root,text="AC",font="Calibri",width=5,command= lambda: AC()).grid(row=3,column=3,columnspan=2,sticky=W+E,padx=5,pady=5)

boton6 = Button(root,text="6",font="Calibri",width=5,command= lambda: click('6')).grid(row=4,column=2,padx=5,pady=5)
boton5 = Button(root,text="5",font="Calibri",width=5,command= lambda: click('5')).grid(row=4,column=1,padx=5,pady=5)
boton4 = Button(root,text="4",font="Calibri",width=5,command= lambda: click('4')).grid(row=4,column=0,padx=5,pady=5)
botonMult = Button(root,text="*",font="Calibri",width=5,command= lambda: fun('*',1)).grid(row=4,column=3,padx=5,pady=5)
botonDiv = Button(root,text="/",font="Calibri",width=5,command= lambda: fun('/',1)).grid(row=4,column=4,padx=5,pady=5)

boton3 = Button(root,text="3",font="Calibri",width=5,command= lambda: click('3')).grid(row=5,column=2,padx=5,pady=5)
boton2 = Button(root,text="2",font="Calibri",width=5,command= lambda: click('2')).grid(row=5,column=1,padx=5,pady=5)
boton1 = Button(root,text="1",font="Calibri",width=5,command= lambda: click('1')).grid(row=5,column=0,padx=5,pady=5)
botonSum = Button(root,text="+",font="Calibri",width=5,command= lambda: fun('+',1)).grid(row=5,column=3,padx=5,pady=5)
botonRes = Button(root,text="-",font="Calibri",width=5,command= lambda: fun('-',1)).grid(row=5,column=4,padx=5,pady=5)

boton0 = Button(root,text="0",font="Calibri",width=5,command= lambda: click('0')).grid(row=6,column=0,padx=5,pady=5)
botonPunto = Button(root,text=".",font="Calibri",width=5,command= lambda: click('.')).grid(row=6,column=1,padx=5,pady=5)
botonIgual = Button(root,text="=",font="Calibri",width=5,command= lambda: igual()).grid(row=6,column=2,padx=5,pady=5)
botonResta = Button(root,text="(-)",font="Calibri",width=5,command= lambda: Resta('-')).grid(row=6,column=3,padx=5,pady=5)
botonExp = Button(root,text="^",font="Calibri",width=5,command= lambda: fun('^',1)).grid(row=6,column=4,padx=5,pady=5)




root.mainloop()
