def texto_a_binario(texto):
    # Convierte cada carácter del texto a su representación binaria
    return ' '.join(format(ord(caracter), '08b') for caracter in texto)

# Pide al usuario que ingrese el texto


with open("texto.txt", "r")as p:
   p = p.read()
   print("Leido")






texto = p #= input("Escribe tu texto: ")

# Convierte el texto a binario
resultado_binario = texto_a_binario(texto)

# Muestra el resultado





with open("codigo.txt", "w")as c:
    c = c.write(resultado_binario)
    print("exito")

