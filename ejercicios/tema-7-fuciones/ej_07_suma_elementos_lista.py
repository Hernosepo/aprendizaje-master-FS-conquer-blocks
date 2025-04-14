
def suma_lista(lista):
    suma = 0
    for num in lista:
        suma += num
    return suma

resultado = suma_lista([1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9])
print(resultado)