
'''CLASE PERSONA 
Define una clase Persona con atributos como nombre, edad y profesión. 
Luego, crea varios objetos de esta clase y muestra su información.'''

class Persona:
    def __init__ (self,nombre,edad,profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
personas = Persona('Hernan','38','Desocupado')
print(f'{personas.nombre}, {personas.edad}, {personas.profesion}')

'''CALCULADORA BÁSICA 
Crea una clase llamada "Calculadora" con métodos para sumar, restar, 
multiplicar y dividir. Crea objetos de esta clase y realiza algunas operaciones 
básicas.'''

class Calculadora:
    def suma(self, numuno, numdos):
        return numuno + numdos
    def resta(self, numuno, numdos):
        return numuno - numdos
    def mult(self, numuno, numdos):
        return numuno * numdos
    def div(self, numuno, numdos):
        return numuno / numdos

calculos = Calculadora()
print(calculos.suma(4,4))
print(calculos.resta(4,4))
print(calculos.mult(4,4))
print(calculos.div(4,4))

'''LIBRO 
Crea una clase "Libro" con atributos como título, autor y año de publicación. 
Luego, crea varios objetos Libro y muestra su información.'''

class Libro:
    def __init__(self,titulo,autor,publicacion):
        self.titulo = titulo
        self.autor = autor
        self.publicacion = publicacion
    def impresion(self):
        return (f'El libro {self.titulo} pertenece a {self.autor} y fue publicado en {self.publicacion}')
piedrafilosofal = Libro('H. P. y la piedra filosofal','J. K. Rowling',1997)
print(piedrafilosofal.impresion())

'''RECTÁNGULO 
Crea una clase "Rectangulo" con atributos de longitud y ancho. Implementa 
un método para calcular el área y el perímetro del rectángulo.'''

class Rectangulo:
    def __init__(self,long,width):
        self.long = long
        self.width = width
    def area(self):
        return (self.long * self.width)
    def perimetro(self):
        return 2 * (self.long + self.width)
calculo_rectangulo = Rectangulo(2,3)
print(calculo_rectangulo.area())
print(calculo_rectangulo.perimetro())

'''DADO 
Crea una clase "Dado" que simule el lanzamiento de un dado de 6 caras. 
Implementa un método para lanzar el dado y mostrar el resultado (quizás te 
convenga usar el modulo random).'''
import random
class Dado:
    def roll_dado(self):
        return random.randint(1,6)
roll = Dado()
print('Ha salido:', roll.roll_dado())    

'''COCHE 
Crea una clase "Coche" con atributos como marca, modelo y año. 
Implementa un método para encender el Coche y otro para apagarlo (puedes 
simulae el encendido y apagado con una variable booleana). '''


class Coche:
    def __init__(self,marca,modelo,year):
        self.marca = marca
        self.modelo = modelo
        self.year = year
        self.arranque = False
    def arrancar (self):
        self.arranque = True
    def parar(self):
        self.arranque = False    

auto_uno = Coche('BMW', 'Serie 3', 1987)
auto_dos = Coche('Fiat', 'Palio', 2005)

print(auto_uno.marca, auto_uno.modelo, auto_uno.year, auto_uno.arranque)
auto_uno.arrancar()
print(auto_uno.marca, auto_uno.modelo, auto_uno.year, auto_uno.arranque)

        