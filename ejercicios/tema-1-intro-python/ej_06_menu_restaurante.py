
'''RESTAURANTE:
En un restaurante el menú consta de las siguientes opciones:
Ensalada mixta ———————— 12 EU
Sopa de pescado ——————— 10 EU
Dorada al horno ———————— 18 EU
Arroz al curry ————————— 14 EU
Lasaña de carne ——————— 15 EU
Brownie de chocolate ————— 8 EU
Helado ——————————— 6 EU
Refrescos —————————— 5,5 EU
Café ———————————— 3,5 EU
Escribe un script que lea la cantidad de cada alimento consumido y que calcule e imprima el total
de la cuenta.'''

nensalada = float(input("Nro de Ensalada Mixta: "))
nsopa = float(input("Nro de Sopa de Pescado: "))
ndorada = float(input("Nro de Dorada al Horno: "))
narroz = float(input("Nro de Arroz al Curry: "))
nlasana = float(input("Nro de Lasaña de Carne: "))
nbrownie = float(input("Nro de Brownie de Chocolate: "))
nhelado = float(input("Nro de Helado: "))
nrefrescos = float(input("Nro de Refrescos: "))
ncafe = float(input("Nro de Cafes: "))

pensalada = 12.0 * nensalada
psopa = 10.0  * nsopa
pdorada = 18.0 * ndorada
parroz = 14.0 * narroz
plasana = 15.0 * nlasana
pbrownie = 8.0 * nbrownie
phelado = 6.0 * nhelado
prefrescos = 5.5 * nrefrescos
pcafe = 3.5 * ncafe

cuentaTotal = pensalada + psopa + pdorada + parroz + plasana + pbrownie + phelado + prefrescos + pcafe

print("Su cuenta es: $", cuentaTotal)