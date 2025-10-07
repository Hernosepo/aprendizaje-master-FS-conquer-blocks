'''LISTAS DE CARACTERES:
1. Crea una lista llamada frutas que contengan los siguientes nombres de frutas como cadenas
de caracteres: manzana, plátano, cereza, pera, higo, frambuesa y fresa.
2. Usa la función len() para imprimir la longitud de la lista frutas.
3. Accede al objeto numero 3 de la lista e imprímelo por consola.
4. Modifica el segundo objeto de la lista y cambiado a mora.
5. Añade el string mango al final de la lista.
6. Usa el método insert() y añade el string “uva“ año comienzo de la lista.
7. Usa un bucle para recorrer la lista e imprimir cada fruta por la consola
8. Usa el método pop() para eliminar el último elemento de la lista y guárdalo en una variable
llamada “ultima_fruta“.
9. Realiza un bucle que recorra la lista e imprima cada una de las frutas por consola
10. Modifica el script para que imprima también la longitud de cada nombre de fruta por consola
11. Modifica el script para que recorra la lista de frutas y solo imprima aquellos nombres que
tengan más de 5 caracteres
12. Usa el método remove() para borrar el string “cereza“ de la lista.
13. Usa el método clear() para vaciar la lista.
Recomendación: En cada paso comprueba que el código hace aquello que quieres'''

frutas = ["manzana", "platano", "cereza", "pera", "higo", "frambuesa", "fresa"]

print(len(frutas))
print(frutas[2])

frutas_mora = ["manzana", "platano", "cereza", "pera", "higo", "frambuesa", "fresa"]
frutas_mora[1] = "mora"
print(frutas_mora)

frutas_mora.append("mango")
print(frutas_mora)
frutas_mora.insert(0,"uva")
print(frutas_mora)

for i in frutas_mora:
    print(i)

ultima_fruta = frutas_mora.pop()
print(frutas_mora)
print(ultima_fruta)

for i in frutas_mora:
    print(i)

for i in frutas_mora:
    print(len(i))    

for i in frutas_mora:
    if len(i) > 5:
        print(i)

frutas_remove =  ['uva', 'manzana', 'mora', 'cereza', 'pera', 'higo', 'frambuesa', 'fresa', 'mango']
frutas_remove.remove("cereza")

frutas_clear =  ['uva', 'manzana', 'mora', 'cereza', 'pera', 'higo', 'frambuesa', 'fresa', 'mango']
frutas_clear.clear()
print(frutas_clear)