'''CUENTA BANCARIA 
Crea una clase "CuentaBancaria" con atributos como número de cuenta y 
saldo. Implementa métodos para depositar y retirar dinero, y muestra el 
saldo actual.'''

from datetime import date

class CuentaBancaria:
    def __init__(self, titular, nro_cuenta):
        '''titular, nro de cuenta, saldo, fecha de ultima operacion, retiro, deposito'''
        self.titular = titular
        self.nro_cuenta = nro_cuenta
        self.ultima_operacion = date.today()
        self.saldo = 0
    #def consulta(self):
    #    return (f'Titular:{self.titular}\nNro de cuenta:{self.nro_cuenta}\nSaldo:{self.saldo}\nUltima operacion:{self.ultima_operacion}')    

    def depositar(self, cantidad):
        self.saldo += cantidad
        return (f'Titular:{self.titular}\nNro de cuenta:{self.nro_cuenta}\nSaldo:{self.saldo}\nUltima operacion:{self.ultima_operacion}\nDeposito: {cantidad}')
    
    def retirar(self, cantidad):
        self.saldo -= cantidad
        return (f'Titular:{self.titular}\nNro de cuenta:{self.nro_cuenta}\nSaldo:{self.saldo}\nUltima operacion:{self.ultima_operacion}\nRetiro: {cantidad}')

         

estado_de_cuenta = CuentaBancaria('Hernan Geller',293212)

print(estado_de_cuenta.depositar(100))
print(estado_de_cuenta.retirar(10))

