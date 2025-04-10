'''PALABRAS PROHIBIDAS:
Define una lista de 5 palabras aleatorias y una lista de letras prohibidas que contenga tres letras.
Filtra las palabras en tu lista original crea una nueva lista de palabras filtradas que solo contenga
aquellas palabras que no tienen ninguna letra prohibida.'''

palabras = ["manzana", "casa", "bonito", "toro", "acronimo"]
letras = ["a","b","c"]
palabras_sinletras = [] 

for palabra in palabras: 
    la_bandera = True
    for letra in palabra: 
        if letra in letras: 
            la_bandera = False

    if la_bandera:
        palabras_sinletras.append(palabra) 
print(palabras_sinletras)
    