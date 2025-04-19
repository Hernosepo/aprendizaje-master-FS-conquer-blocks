class Pila:
    def __init__(self):
        self.apilador = []

    def agregar_pila(self, apila):
        self.apilador.append(apila)
        
    def sacar_pila(self):
        self.apilador.pop()

    def mostrar_pila(self):
        print(self.apilador)

apilar = Pila()

apilar.agregar_pila(1)
apilar.mostrar_pila()
apilar.agregar_pila(4)
apilar.agregar_pila(5)
apilar.agregar_pila(9)
apilar.mostrar_pila()
apilar.sacar_pila()
apilar.mostrar_pila()