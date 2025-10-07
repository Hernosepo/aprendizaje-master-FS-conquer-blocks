'''CONTRASEÑA SEGURA:
Por motivos de seguridad una contraseña debe tener una vocal en minúscula, dos símbolos
especiales diferentes (pueden ser solo * o #). Dada una contraseña ingresada por el usuario,
comprueba si es una contraseña segura e indícalo por pantalla.'''


# Pedir contraseña
password_in = input("Ingrese su contraseña: ")

# Analizar string de contraseña
if ("a" in password_in) or ("e" in password_in) or ("o" in password_in) or ("u" in password_in) and ("*" in password_in) or ("#" in password_in):
    print("Su contraseña es segura")
else:
    print("Su contraseña necesita ser reforzada")    

