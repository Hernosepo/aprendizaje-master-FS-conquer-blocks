'''BIENVENIDA AL USUARIO:
Un ordenador tiene tres usuarios distintos (Alejandro, Naomi y Sergio) y otro usuario invitado.
Haz un script que pida el nombre al usuario y le dé una bienvenida personalizada. Crea el script
de tal manera que si el usuario no es ninguno de los tres se le dé un saludo genérico.
¿Que ocurre si uno de los usuarios introduce su nombre completamente en minúsculas?¿Y si lo
introduce en mayúsculas? ¿Y si sin querer pone in punto en mitad de su nombre (p.e. nao.mi)?¿Y
si se le cuela una almohadilla (p.e se#rgio)?'''

# Pedir nombre de usuario
nombre_ingreso = input("Hola! ¿Cual es tu nombre?\n")
caracteres_a_remover = "!#$%&/()=?¡'.,:;><"

# Analizar input
# Devolver saludo personalizado
if nombre_ingreso.title().strip().translate(str.maketrans('', '', caracteres_a_remover)).lower() == "alejandro":
    print("Bienvenido Alejandro!")
elif nombre_ingreso.title().strip().translate(str.maketrans('', '', caracteres_a_remover)).lower() == "naomi":
    print("Bienvenida Naomi!")
elif nombre_ingreso.title().strip().translate(str.maketrans('', '', caracteres_a_remover)).lower() == "sergio":
    print("Bienvenido Sergio!")
# Devolver saludo generico
else:
    print("Bienvenido che! Registrate y te saludo apropiadamente!")




