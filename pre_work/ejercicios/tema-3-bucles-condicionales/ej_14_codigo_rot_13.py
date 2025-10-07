'''ENCRIPTACIÓN ROT13:
El abecedario latino es un sistema de escritura alfabético más usado del mundo hoy en día. Se
compone de 26 letras principales, más ciertas modificaciones y letras adicionales según el idioma
del que se trate (por ejemplo, en castellano y gallego se incluye la ”ñ”, en portugués, francés y
catalán la ”Ç”, en alemán la ”ß”, etc.).
Aplicar el cifrado ROT13 a un texto se reduce a examinar sus caracteres alfabéticos y sustituirlos
por la letra que está 13 posiciones por delante en el alfabeto, volviendo al principio si es necesario
y conservando las mayúsculas y minúsculas: a se convierte en n, B se convierte en O, y así hasta
la Z, que se convierte en M. Solo quedan afectadas las 26 letras principales que aparecen en el
alfabeto latino; los números, símbolos, espacios y otros caracteres se dejan igual.
1. Desarrolla un script que recibiendo de entrada una cadena de caracteres devuelva el texto
codificado según el cifrado ROT13
2. Desarrolla ahora un script que compare dos cadenas de caracteres y nos diga si una de ellas
esta codificación ROT13 de la otra.'''


string_prueba = "soy hincha de racing"
string_vuelta = "fbl uvapun qr enpvat"
abecedario = "abcdefghijklmnopqrstuvwxyz"
abecedario_mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mensaje_cripto = ""

for letra in string_vuelta:
    if letra in abecedario:
        indice_original = abecedario.index(letra)
        nuevo_indice = (indice_original + 13) % 26
        nueva_letra = abecedario[nuevo_indice]
        mensaje_cripto += nueva_letra
    else:
        mensaje_cripto += letra    
print(mensaje_cripto)        