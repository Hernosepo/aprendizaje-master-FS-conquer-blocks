'''BASE DE DATOS DE UN COLEGIO:
Trabajas en un colegio y estas encargado de mantener un seguimiento de las notas de los
estudiantes de una clase. En tu base de datos tienes una lista con los nombres de los estudiantes y
para cada estudiante debes guardar sus notas provenientes de deberes, exámenes y proyectos.
También necesitas calcular a nota media de cada estudiante y la nota media de la clase al
completo.'''

alumnos_notas = [
    ["Manuel García", 7.5, 8.0, 9.0],
    ["Juan Pérez", 6.0, 6.5, 7.0],
    ["Lucía Romero", 9.0, 8.5, 9.5],
    ["Valentina Díaz", 5.5, 6.0, 6.5],
    ["Carlos Méndez", 8.0, 7.5, 8.0]
]
calculo_promedio = 0
promedio_general = 0

for nota_individual in alumnos_notas:   # itero por las sublistas
    calculo_promedio = (float(nota_individual[1]) + float(nota_individual[2]) + float(nota_individual[3])) / 3.0 # tomo los valores para dividir y sacar el promedio
    nota_individual.append(calculo_promedio) # agrego el promedio al final de la lista "SEGUN ENTENDI DE TU PISTA 1 ESTABA AGREGANDO calculo_promedio AL FINAL DE LA LISTA GENERAL"
    promedio_general = promedio_general + calculo_promedio # sumo para obtener el total de promedios
for alumno in alumnos_notas: # ingreso a la sublista nuevamente para imprimir los resultados
    notas = "El alumno ", alumno[0], " ha obtenido:  ", alumno[1], " en deberes, ", alumno[2], " en examenes, ", alumno[3], " en proyectos. Su promedio es: ", alumno[4] # no estoy accediento correctamente a los datos
    print(notas) # aunque correcto no me gusta como quedo la impresion

print(promedio_general / len(alumnos_notas)) # divido por el largo de la lista para sacar el promedio general
