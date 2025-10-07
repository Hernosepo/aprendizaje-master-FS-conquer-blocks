'''SISTEMA DE GESTIÓN DE EMPLEADOS'''

class Empleado:
    def __init__(self, nombre, apellido, salario):
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario


class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, apellido, salario, bono_anual):
        super().__init__(nombre, apellido, salario)

        self.bono_anual = bono_anual

    def calculo_bono(self):
        return self.salario + self.bono_anual            


class EmpleadoTiempoParcial(Empleado):
    def __init__(self, nombre, apellido, salario, semana_hora):
        super().__init__(nombre, apellido, salario)

        self.semana_hora = semana_hora

    def calculo_horas_trabajadas(self):
        return 12 * 4 * self.salario * self.semana_hora 


empleado_full = EmpleadoTiempoCompleto('Hernan', 'Geller', 2000, 500)
print("Total:", empleado_full.calculo_bono())

empleado_half = EmpleadoTiempoParcial('Maria', 'Lopez', 20, 12)
print("Total:", empleado_half.calculo_horas_trabajadas())


