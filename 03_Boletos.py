
n = 0
sumatoria1 = int(input("Ingrese la sumatoria: "))
i = 0
sumatoria2 = 0
c = sumatoria1


while sumatoria1>0:
    i += 1
    sumatoria1 -=i
    if sumatoria1 <0:
        print("Numero inexacto: {}".format(i-1))
        n = i-1
    elif sumatoria1 ==0:
        print("Numero exacto: {}".format(i))
        n = i

for i in range(1, n+1):
    sumatoria2 += i
restante = c-sumatoria2
print("La sumatoria es : {}".format(sumatoria2))
print("Restante = {} - {} = {}".format(c,sumatoria2,restante))








