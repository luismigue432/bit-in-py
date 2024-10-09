def binario_a_texto(binario):
    # Divide la cadena de binarios en grupos de 8
    caracteres_binarios = binario.split()
    texto = ''.join(chr(int(b, 2)) for b in caracteres_binarios)
    return texto

# Pide al usuario que ingrese la cadena de números binarios


with open("codigo.txt", "r")as c:
    c = c.read()
    print("exito")

binario = c
# Convierte la cadena binaria a texto
resultado_texto = binario_a_texto(binario)




# Muestra el resultado
print("Texto resultante:", resultado_texto)
