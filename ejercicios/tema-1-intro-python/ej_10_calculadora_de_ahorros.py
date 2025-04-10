'''CALCULADORA DE AHORROS:
Ahora que ya tienes soltura con los fundamentos de Python toca poner tus conocimientos en
práctica en un proyecto más extenso. El objetivo es crear un programa con el que puedas calcular
tus ahorros anuales. El programa deberá calcular cuánto puede ahorrar una persona dado sus
ingresos por hora, sus horas trabajadas y su gasto de vida semanal.
1. Primero haremos que el programa nos pida nuestro nombre y después imprima un saludo por
pantalla de tipo: Hola <Nombre>
2. Guarda el dinero ganado por hora y las horas trabajadas en la semana en dos variables
diferentes
3. Multiplica ambas variables para obtener el salario semanal
4. Ahora calcula las ganancias anuales. Guarda el valor en una variable.
5. Ahora imprime por pantalla un mensaje del tipo: <Nombre> tiene unas ganancias anuales de:
<cantidad> euros
6. Pide los gastos semanales por pantalla y guárdalos en una variable.
7. Calcula el gasto anual
8. ¡Recuerda añadir comentarios sobre lo que esta haciendo cada parte del código!
9. Los ahorros anuales serán la resta entre lo ganado durante el año menos los gastos anuales.
10. Imprime los resultados por pantalla
¿Si el usuario decidiese trabajar a tiempo parcial (25 horas semanales) y decidiese reducir sus
gastos a 3/4 de lo que gastaba antes, tendría suficiente dinero para sus gastos?
(Pista: tan solo necesitas cambiar los valores de las variables de horas trabajadas por semana y
gastos semanales)'''


# Pedir nombre del usuario
nombreUsr = str(input("Hola! ¿Cual es tu nombre?\n"))

# Imprimir saludo al usuario
print("Hola! Bienvenido ", nombreUsr.title())

# Pedir salario por hora y horas semanales trabajadas
salario_hora = int(input("¿Cual es tu salario por hora? - "))
horas_semana = int(input("¿Cuantas horas trabajas por semana? - "))

# Obtener salario semanal
salario_semana = salario_hora * horas_semana

# Obtener salario anual
salario_anual = salario_semana * 52

# Pedir gastos semanales
gasto_semanal = float(input("¿Cuanto gastas por semana? - "))

# Obtener gasto anual
gasto_anual = gasto_semanal * 52

# ------Info para el usuario-------

# Salario semanal
print(nombreUsr.title(), "actualmente ganas: ", salario_semana, " euros por semana")

# Salario anual
print("Actualmente ganas: ", salario_anual, " euros por año")

# Gasto anual
print("Actualmente tu gasto anual es de: ", gasto_anual, " euros por año")

# Ahorro anual
print("Por ende tu ahorro es de: ", salario_anual - gasto_anual, " euros")