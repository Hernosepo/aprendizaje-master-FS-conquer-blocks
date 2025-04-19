'''SISTEMA DE RESERVAS DE VUELOS'''

class Vuelo:
    def __init__(self, nro_vuelo, origen, destino, cap_maxima):

        self.nro_vuelo = nro_vuelo
        self.origen = origen
        self.destino = destino
        self.cap_maxima = cap_maxima
        self.lista_pasajeros = []

    def check_disponibilidad(self):
        return self.cap_maxima - len(self.lista_pasajeros)    

    def agregar_pasajero(self, nuevo_pasajero):
        if self.check_disponibilidad() > 0:
            self.lista_pasajeros.append(nuevo_pasajero)
            print(f"Pasajero {nuevo_pasajero} agregado al vuelo {self.nro_vuelo}")
        else:
            print('Capacidad maxima alcanzada')    



class VueloEspecial(Vuelo):
    def __init__(self, nro_vuelo, origen, destino, cap_maxima, motivo_vuelo_especial):
        super().__init__(nro_vuelo, origen, destino, cap_maxima)

        self.motivo_vuelo_especial = motivo_vuelo_especial


vuelo_regular = Vuelo("XXX000", "AA", "BB", 100)
vuelo_regular.agregar_pasajero("Juan")
print("Asientos disponibles:", vuelo_regular.check_disponibilidad())        


vuelo_especial = VueloEspecial("YYY111", "CC", "DD", 150, "Vacaciones")
vuelo_especial.agregar_pasajero("Laura")
print("Asientos disponibles en el vuelo especial:", vuelo_especial.check_disponibilidad())
print("Motivo del vuelo especial:", vuelo_especial.motivo_vuelo_especial)