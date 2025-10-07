
'''1. Define una función llamada "saludar" que tome un parámetro "nombre" y muestre un saludo personalizado.'''

def saludar(nombre):
    saludo = print("Hola!", nombre)
    return saludo

saludar("Hernán")

'''2. Crea una función llamada "suma" que tome dos parámetros "a" y "b" e imprima la suma de ambos.'''

def suma(a,b):
    calculo = a + b
    print(calculo)

suma(7,8)

'''3. Escribe una función llamada "calcular_area_rectangulo" que tome dos parámetros "base" y "altura" y calcule el 
área de un rectángulo.'''

def calcular_area_rectangulo(base,altura):
    area = base * altura
    return area

resultado_area = calcular_area_rectangulo(base=3,altura=8)
print(resultado_area)

'''4. Define una función llamada "imprimir_lista" que tome una lista como parámetro y la imprima en la consola.'''

def imprimir_lista(lista):
    print(lista)

una_lista = [1,2,3,4,5,6,7,8,9,0]
imprimir_lista(una_lista)    

'''5. Crea una función llamada "es_par" que tome un número como parámetro e imprima True si es par, o False si es impar.'''

def es_par(num):
    if num % 2 == 0:
        print(True)
    else:
        print(False)    
es_par(9)

'''6. Escribe una función llamada "concatenar_strings" que tome dos parámetros "cadena1" y “cadena2" e imprima la 
concatenación de ambas cadenas.'''

def concatenar_strings(cadena1,cadena2='Gomez'):
    print(f'{cadena1} {cadena2}')

concatenar_strings(cadena1='Juan')

'''7. Define una función llamada "obtener_maximo" que tome una lista de números como parámetro y devuelva el 
número máximo de la lista.'''
    
def obtener_maximo(lista):
    print(max(lista))

lista = [1,2,3,4,5,6,7,8,9,0]
obtener_maximo(lista)

'''8. Crea una función llamada "convertir_fahrenheit_a_celsius" que tome un parámetro "fahrenheit" y 
devuelva su equivalente en grados Celsius.'''

def convertir_fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) / 0.5556
    print(celsius)

convertir_fahrenheit_a_celsius(32)

'''9. Escribe una función llamada "calcular_edad" que tome dos parámetros: "año_actual" y "año_nacimiento" 
y calcule la edad de una persona.'''

def calcular_edad(año_actual,año_nacimiento):
    print(año_actual - año_nacimiento)

calcular_edad(año_actual=2025,año_nacimiento=1987)    

'''10. Define una función llamada "es_divisible" que tome dos parámetros "num" y "divisor" e imprima True si 
"num" es divisible por "divisor", o False si no lo es.'''
def es_divisible(num, divisor):
    if num % divisor == 0:
        resultado = True
    else:
        resultado = False
    print(resultado)

es_divisible(25,8)

'''11. Crea una función llamada "mostrar_info_persona" que tome tres argumentos de palabra clave: 
"nombre", "edad" y "ciudad". La función debe imprimir en la consola la información de una persona 
en un formato legible.'''

def mostrar_info_persona(nombre, edad, ciudad):
    print(f'Nombre: {nombre} Edad: {edad} Ciudad: {ciudad}')

mostrar_info_persona(nombre = "Robert", edad = 32, ciudad = "Paraguay")

'''12. Escribe una función llamada "calcular_promedio" que tome una lista de números como parámetro y calcule el 
promedio de esos números. Si no se proporciona una lista, debe usar una lista vacía por defecto.'''

'''13. Crea una función llamada "calcular_potencia" que tome dos parámetros "base" y "exponente", y 
calcule la potencia de la base elevada al exponente. Utiliza 2 como valor por defecto para el exponente.'''

'''14. Define una función llamada "imprimir_info_alumno" que tome un argumento posicional “nombre”
(y sin valor por defecto) y varios argumentos de palabra clave: "edad", "curso" y “promedio" (puedes 
ponerles como valor por defecto None). La función debe imprimir la información del alumno en un formato legible.'''