'''LISTA DE TAREAS 
Crea una clase "ListaTareas" que contenga una lista de tareas pendientes. 
Implementa métodos para agregar una tarea, marcar una tarea como 
completada y mostrar todas las tareas'''

class LstaTareas:
    def __init__(self, tareas):
        self.tareas = tareas
        self.realizada = []
    
    def tarea_agregar(self, tarea):
        self.tareas.append(tarea)
        
    def tarea_realizada(self, tarea):
        for tarea in self.tareas:
            if tarea in self.tareas:
                self.realizada.append(tarea)
            elif tarea not in tareas:
                print('La tarea no existe')


    def tareas_compiladas(self):
        pass

tareas = ['Limpiar', 'Estudiar', 'Cocinar', 'Mandar mails']
listado = LstaTareas(tareas)
listado.tarea_agregar('Ejercitar')
listado.tarea_realizada('Armar')






