'''VALIDACION DE FORMULARIO'''

def validar_formulario(nombre,correo_electronico,telefono):
    band_n, band_c, band_t = False, False, False

    if len(nombre) < 3:
        print('Su nombre debe tener al menos tres caracteres')
    else:
        band_n = True
        print(f'Nombre: {nombre}')
    if '@' and '.' in correo_electronico:
        band_c = True
        print('Correo electronico: valido ')
    else:
        print('Correo invalido')
    if len(telefono) != 9:
        print('Telefono invalido')
    else:
        band_t = True
        print('telefono valido')

    if band_n == True and band_c == True and band_t == True:
        print('Formulario Valido')
    else:
        print('Formulario invalido')        



validar_formulario('Hernan','go@go.com','55444444')