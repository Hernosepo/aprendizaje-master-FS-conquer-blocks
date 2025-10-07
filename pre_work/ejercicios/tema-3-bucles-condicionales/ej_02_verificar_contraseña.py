'''2. Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.'''

# Pedir ingreso de contraseña
crear_password = input("Ingrese su contraseña nueva: ")

# Pedir confirmación de contraseña ingresada
confirm_password = input("Confirme su nueva contraseña: ")

# Analizar si las contraseñas coinciden
intentos = 3
for i in range(intentos,0,-1):
    if crear_password != confirm_password:
        print("Las contraseñas no coinciden le quedan", intentos, "oportunidades")
        confirm_password = input("Confirme su nueva contraseña nuevamente: ")
        intentos = intentos - 1
else:
    if crear_password == confirm_password:
        print("Contraseña actualizada\n\n")
        ingresar_password = crear_password
if intentos == 0:
    exit("Se terminaron tus oportunidades")
            
# Si coninciden pedir contraseña
while (input("Ingrese su contraseña A: ")) != crear_password:
    print("Password Incorrecto \n Intente Nuevamente")
# Si la contraseña es correcta imprimir bienvenido
print("Bienvenido")
# Mientras la contraseña sea incorrecta seguir pidiendo la contraseña