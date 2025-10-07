# importamos nuestros modulos
import ej_04_contrasena_segura_validador
import ej_04_contrasena_segura_generador

# funcion que contiene el codigo principal
def solicitar_contrasena_segura():
    """Solicitaremos la contraseña al usuario,
    llamaremos a la funcion validadora y a la funcion
    generadora de nuevas contraseñas si fuese necesario """

    # pedimos contrasena al usuario
    contrasena = input("Ingrese una contrasena: ")
    # validamos la contrasena 
    valida = ej_04_contrasena_segura_validador.validar_contrasena(contrasena)
 
    if valida:
        print("Contrasena segura")

    else:
        # si la contrasena no es valida llamamos a la funcion generadora
        # y sugerimos una nueva contrasena
        print("La contrasena no es segura. Se sugiere una nueva contrasena")
        sugerencia = ej_04_contrasena_segura_generador.generar_contrasena_segura(9)
        print("Sugerencia de contrasena: ", sugerencia)

# Ejemplo de uso
solicitar_contrasena_segura()