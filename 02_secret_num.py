import random

secret_num = random.randint(1,100)


print('""""""Bienvenido a al juego número secreto""""""')
print("Tienes que adivinar un número entre el 1-100")


while True:
    opcion = int(input("Para comenzar presiona escribe un 1 o para salir un 0:"))
    if opcion == 0:
        break
    elif opcion == 1:
        while True:
            n = int(input("Ingresa un numero: "))
            if n < secret_num:
                print("El numero secreto es mayor.")
            elif n > secret_num:
                print("El numero secreto es menor.")
            elif n == secret_num:
                print("Has encontrado el número secreto: {}".format(secret_num))
                print("Has ganado")
                break