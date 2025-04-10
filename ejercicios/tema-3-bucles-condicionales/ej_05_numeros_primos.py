'''NUMEROS PRIMOS 1: Crea un programa que imprima todos los números primos entre el 2 y el 100. Un numero primo es
un numero positivo y entero mayor que uno que no tiene un divisor positivo y entero que no sea 1
o sí mismo.'''

for i in range(2,101):
    primo = True
    for div in range(2,i):
        if i % div == 0:
            primo = False
    if primo:
        print(i)