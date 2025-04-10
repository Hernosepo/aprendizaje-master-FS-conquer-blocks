
mi_diccionario = {}
mi_diccionario['nombre'] = 'Hernan'
print(mi_diccionario['nombre'])
print('edad' in mi_diccionario)
estudiante = {
    'nombre' : 'Juan',
    'edad' : 20,
    'materia' : 'recreo',
}
estudiante['edad'] = 25
del estudiante['materia']
print(estudiante)
agenda = {
    'Juan' : '1234567890',
    'Joana' : '09876543210',
    'Jimena' : '5555555555',
}
agenda['Julio'] = '9998887777'
print(len(agenda))
claves = list(agenda)
print('Juan' in agenda)
del agenda['Jimena']
for nombre, numero in agenda.items():
    print('Nombre:',nombre, "Numero:", numero)
print(agenda.get('Juan', 'Clave no encontrada'))
del agenda
estudiantes = [{
    'nombre' : 'Juan',
    'edad' : 20,
},
{
    'nombre' : 'Pedro',
    'edad' : 19,
}]
estudiantes.append({'nombre':'Eduardo', 'edad':22})
estudiantes.pop(1)
print(estudiantes)
estudiantes[0]['edad'] = 25
print(estudiantes)

productos = {
    'Refresco': {
        'nombre' : 'Sprite',
        'precio' : 4,
    },
    'Vino' : {
        'nombre' : 'Malbec',
        'precio' : 9,
    }
}
for producto, info in productos.items():
    print("Producto:", producto)
    print("Nombre:", info['nombre'])
    print("Precio:", info['precio'])

productos['Jugo'] = {'nombre' : 'Naranjada','precio' : 6}

print(productos)

equipos = {
    'Equipo 1': {
        'nombre' : 'Racing',
        'jugadores' : ['Messi', 'Lisandro', 'Chatruc']},
    'Equipo 2': {
        'nombre' : 'Velez',
        'jugadores' : ['Chilavert', 'Flores', 'Assad']
    },
    'Equipo 3' : {
        'nombre' : 'River',
        'jugadores' : ['Enzo', 'Ortega', 'Aimar']
    }
        
}

equipos['Equipo 4'] = {'nombre' : 'Central','jugadores' : ['Ruben', 'Malcorra', 'Poy']}

equipos['Equipo 1']['jugadores'].append('Coco Basile')
print(equipos)