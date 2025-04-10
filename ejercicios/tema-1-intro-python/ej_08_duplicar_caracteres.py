
'''Crea un script que acepte un string de 5 caracteres y devuelva otro string con todos los caracteres
duplicados. Si el input es ‘sbc56’, el output deberá ser ‘ssbbcc5566’'''

# Perdir que usuario escriba 5 caracteres

cincoCar = str(input("Escriba 5 caracteres "))

# Duplicar los 5 caracteres

carSep = ""

for i in cincoCar:
    carSep = carSep + i*2  

# Imprimir resultado

print(carSep)