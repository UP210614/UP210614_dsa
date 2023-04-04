def quicksort(a, primero, ultimo):
    central = (primero+ultimo)//2
    pivote = a[central]
    i = primero
    j = ultimo
    while True:
        while a[i] < pivote:
            i+=1
        while a[j] > pivote:
            j-=1
        if i<=j:
            a[i],a[j] = a[j],a[i]
            i+=1
            j-=1
        if i>j:
            break
    if primero < j:
        quicksort(a,primero,j)
    if(i<ultimo):
        quicksort(a,i,ultimo)
    return a
lista = [5,4,3,8,1]
print(quicksort(lista,0,len(lista)-1))