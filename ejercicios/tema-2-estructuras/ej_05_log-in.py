'''LOG-IN:
Crea un script que pida una contraseña al usuario (el script sabe cual es la contraseña correcta).
Si la contraseña es correcta el script debe darle la bienvenida al usuario. De lo contrario debe
indicarle que la contraseña es incorrecta y darle una segunda oportunidad de introducir la
contraseña. Al segundo fallo debe mostrar un mensaje de error y terminar de ejecutarse.
Cambia el script para que no distinga entre mayúsculas y minúsculas.'''

# Contraseña 
password_usr = "Messi10"

# Pedir Contraseña
password_usr_in = input("Ingrese su contraseña: ")

# Analizar Contraseña
if password_usr == password_usr_in:
    print("Bienvenido!")
else:
    password_usr_in = input("Error, intente nuevamente: ")
    if password_usr == password_usr_in:
        print("Ahora si, bienvenido!")
    else:
        print("Error")    