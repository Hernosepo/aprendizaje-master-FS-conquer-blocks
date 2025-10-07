'''
Idea y razonamiento:

BLOQUE 1 - INICIO
1 Que el programa me pregunte que quiero hacer
    Agregar Tarea
    Agregar Persona
    Asignar Tarea 

BLOQUE 2 - AGREGAR TAREA
1 Que el programa me pregunte el titulo de la tarea
2 Que el programa me pregunte cuantas personas requerirá esa tarea
3.1 Que me pida una descripción
3.2 Fecha de entrega (Acá puedo convertir la fecha a cantidad de dias para la entrega)
  
BLOQUE 3 - ASIGNAR TAREA
1 Que de una "lista" (no necesariamente en el sentido de la funcion) de personas de mi equipo
elija quien es el encargado
2 Que de la misma lista elija al resto del equipo segun la necesidad de la tarea

BLOQUE 4 - AGREGAR PERSONA
1 Que me pida datos de la persona (campos separados)
    Nombre
    Apellido

Me gustaria poder volver para atras si elegí una sección equivocada
Terminada de llenar una sección quiero volver a inicio    

'''
# Estructura de diccionario para las tareas
almacenador_tareas = {
    'administrativa' : {
        'descripcion': 'definir descripcion administrativa',
        'responsable': 'sin definir',
        'equipo_nro' : 3
    },
    'desarrollo' : {
        'descripcion': 'definir descripcion desarrollo',
        'responsable': 'sin definir',
        'equipo_nro' : 4
    },
    'rrhh' : {
        'descripcion': 'definir descripcion rhh',
        'responsable': 'sin definir',
        'equipo_nro' : 1
    }        
}

personal_agregado = {
    'P1' : {
        'nombre' : 'Juan',
        'apellido' : 'Perez'
    },
    'P2' : {
        'nombre' : 'Diego',
        'apellido' : 'Gonzalez'
    },
    'P3' : {
        'nombre' : 'Maria',
        'apellido' : 'Castro'
    },
    'P4' : {
        'nombre' : 'Petra',
        'apellido' : 'Gomez'
    },
    'P5' : {
        'nombre' : 'Jamaica',
        'apellido' : 'Johnson'
    }        
}
contador = 0


# Funcion para menu principal
def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Agregar tarea")
    print("2. Agregar persona")
    print("3. Asignar tarea")
    print("4. Salir")

    opcion = input("Elegí una opción (1-4): ")
    return opcion

# Funciones separadas de cada opcion del menu
# Funcion para agregar tareas en un diccionario verificando primero si existen
def agregar_tarea(almacenador_tareas):
    nombre_tarea = input('Ingresa el nombre de una nueva tarea\n')
    for tarea_ingresada in almacenador_tareas:
        if tarea_ingresada == nombre_tarea:
            return print('La tarea se encuentra en existencia, regresa a menu principal para asignarla.')
        
    if nombre_tarea:
        descripcion_tarea = input('Ingresa una descripcion para la tarea.\n')
        equipo_para_tarea = int(input("Ingresa el personal necesario para esta tarea (aparte del responsable)\n"))
        almacenador_tareas[nombre_tarea] = {
            'descripcion': descripcion_tarea,
            'responsable': 'sin definir',
            'equipo_nro' : equipo_para_tarea
        }
    return print('La tarea: ', nombre_tarea, ' ha sido agregada con exito')            


# Funcion para agregar personas en un diccionario con un ID progresivo, verificando que se ingresen datos
def agregar_persona(contador,personal_agregado):
    nombre_persona = ''
    apellido_persona = ''
    while nombre_persona == '' or apellido_persona == '':
        nombre_persona = input('Ingresa nombre\n')
        apellido_persona = input('Ingresa apellido\n')
        if nombre_persona == '' or apellido_persona == '':
            print('Los datos no son correctos')
        else:
            contador += 1
            string_id = 'P' + str(contador)    
        personal_agregado[string_id] = {'nombre': nombre_persona, 'apellido':apellido_persona}
        return print(nombre_persona +' '+ apellido_persona, 'ha sido agregado correctamente')


# Funcion para asignar tareas tomando los diccionarios de tareas y personal
def asignar_tarea(almacenador_tareas,personal_agregado):
    print('\n ---- LISTA DE TAREAS ----')
    for listado_tarea_actual in almacenador_tareas:
        print(listado_tarea_actual)

    # El usuario escribe la tarea que quiere seleccionar y se aloja en tarea_seleccionada
    tarea_seleccionada = input('Selecciona la tarea a designar:')
    tarea_valida = False
    # Chequeo seleccion es la variable de iteracion de las claves en almacenador de tareas
    for chequeo_eleccion_tarea in almacenador_tareas:
        if not tarea_valida:
            if chequeo_eleccion_tarea == tarea_seleccionada:
                print('Seleccionaste: ', tarea_seleccionada)
        else:
            print('La tarea no existe, no es posible asignarla.')
    for personal in personal_agregado:
        nombre = personal_agregado[personal]['nombre']
        apellido = personal_agregado[personal]['apellido']
        print(f'- {personal}: {nombre} {apellido}')             

    # Empiezo la seleccion del encargado pidiendo input de ID
    encargado_seleccion = input('\nIngresa el ID del encargado seleccionado: ')
    encargado_valido = False
    for chequeo_eleccion_encargado in personal_agregado:
        if not encargado_valido:
            if chequeo_eleccion_encargado == encargado_seleccion:
                nombre_encargado = personal_agregado[chequeo_eleccion_encargado]['nombre']
                apellido_encargado = personal_agregado[chequeo_eleccion_encargado]['apellido']            
                print(f'Responsable asignado:, {nombre_encargado} {apellido_encargado},tarea: {tarea_seleccionada}')
        else:
            print('ID inexistente')
    
    # En este bloque agrego los miembros del equipo restantes
    cantidad_equipo = almacenador_tareas[tarea_seleccionada]['equipo_nro']
    equipo_asignado = []
    contador_equipo = cantidad_equipo
    while len(equipo_asignado) < cantidad_equipo:
        print(f'\n---- SELECCIONA {contador_equipo} PERSONAS PARA EL EQUIPO ----')
        for equipo_id in personal_agregado:
            nombre_seleccion = personal_agregado[equipo_id]['nombre']
            apellido_seleccion = personal_agregado[equipo_id]['apellido']
            print(f'- {equipo_id}: {nombre_seleccion} {apellido_seleccion}')
        
        personal_seleccion = input('Selecciona el ID de la persona que integrará el equipo: ')
        
        if personal_seleccion not in personal_agregado:
            print("ID inválido. Intentá nuevamente.")
            continue
        if personal_seleccion in equipo_asignado:
            print("Esa persona ya fue asignada al equipo.")
            continue
        contador_equipo -= 1
        equipo_asignado.append(personal_seleccion)
        print("Integrante agregado. Equipo actual:", equipo_asignado)



# Bucle while para seleccionar las opciones de la funcion menu
while True:
    eleccion = mostrar_menu()

    if eleccion == '1':
        agregar_tarea(almacenador_tareas)
    elif eleccion == "2":
        agregar_persona(contador,personal_agregado)
        contador += 1 
    elif eleccion == "3":
        asignar_tarea(almacenador_tareas,personal_agregado)
    elif eleccion == "4":
        break
    else:
        print("Opción inválida.")
        

