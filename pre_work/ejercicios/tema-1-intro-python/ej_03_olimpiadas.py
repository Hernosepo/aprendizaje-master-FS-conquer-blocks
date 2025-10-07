'''  OLIMPIADAS:
En la competición de skeleton de las olimpiadas de invierno hay tres finalistas. 
El cronómetro mide los siguientes tiempos:
        Hannah Neise: 8 minutos 3 segundos y 10 centésimas
        Jackie Narracott: 12 minutos 7 segundos y 8 centésimas
        Kimberley Bos: 9 minutos 14 segundos y 3 centésimas
1. Crea un script que pida los tiempos por pantalla para cada uno de los finalistas
2. Convierte los tiempos de minutos-segundos-centésimas a segundos
3. Sabiendo que la pista es de 100 metros calcula la velocidad media de cada uno de ellos en metros por segundo.
4. Imprime los resultados por pantalla  '''


# Ingrese el nombre de la competidora y su tiempo:
nombreHanna = str(input("Ingrese el nombre de la corredora 1:\n"))
tiempoHanna = input("Ingrese tiempo de " + nombreHanna + " alcanzado (MM/SS/CC)\n")
nombreJackie = str(input("Ingrese el nombre de la corredora 2:\n"))
tiempoJackie = input("Ingrese tiempo de " + nombreJackie + " alcanzado (MM/SS/CC)\n")
nombreKimberly = str(input("Ingrese el nombre de la corredora 3:\n"))
tiempoKimberly = input("Ingrese tiempo de " + nombreKimberly + " alcanzado (MM/SS/CC)\n")

# Split del tiempo:
minHannaSplit, secHannaSplit, centHannaSplit = tiempoHanna.split("/")
minJackieSplit, secJackieSplit, centJackieSplit = tiempoJackie.split("/")
minKimberlySplit, secKimberlySplit, centKimberlySplit = tiempoKimberly.split("/")

#Conversion a segundos:
segSumaHanna = float(minHannaSplit) * 60 + float(secHannaSplit) + float(centHannaSplit) * 0.1
segSumaJackie = float(minJackieSplit) * 60 + float(secJackieSplit) + float(centJackieSplit) * 0.1
segSumaKimberly = float(minKimberlySplit) * 60 + float(secKimberlySplit) + float(centKimberlySplit) * 0.1

# Velocidad media para la carrera:
velHanna = 100.00 / segSumaHanna
velJackie = 100.00 / segSumaJackie
velKimberly = 100.00 / segSumaKimberly

print("Participante: ", nombreHanna)
print("Tiempo: ", minHannaSplit, " min., ", secHannaSplit, " seg., ", centHannaSplit, " cent.")
print("Velocidad promedio: ", velHanna)

print("Participante: ", nombreJackie)
print("Tiempo: ", minJackieSplit, " min., ", secJackieSplit, " seg., ", centJackieSplit, " cent.")
print("Velocidad promedio: ", velJackie)

print("Participante: ", nombreKimberly)
print("Tiempo: ", minKimberlySplit, " min., ", secKimberlySplit, " seg., ", centKimberlySplit, " cent.")
print("Velocidad promedio: ", velKimberly)