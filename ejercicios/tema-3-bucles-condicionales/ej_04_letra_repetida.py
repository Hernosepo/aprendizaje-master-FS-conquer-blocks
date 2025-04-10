'''4. Crea un programa en el que se pregunte al usuario por una frase y una letra, y muestre por
pantalla el número de veces que aparece la letra en la frase.'''

# Preguntar por una frase
frase_ingresada = input("Escriba una frase: ")

# Preguntar por una letra
letra_elegida = input("Elja una letra: ")

# Recorrer el string y sumar la letra en cada aparicion
largo_frase = len(frase_ingresada)
counter = 0

for i in frase_ingresada:
    if i == letra_elegida:
        counter = counter + 1 
print(counter) 