print("Ingresa el mensaje cifrado")
mensajecifrado = input()
print("Cuántas veces se movio la letra")
veces = int(input())

mensajedescifrado = ""

for i in range(0, len(mensajecifrado), 1):
    letra = mensajecifrado[i]
    minuscula = (letra >= 'a' and letra <= 'z')
    mayuscula = (letra >= 'A' and letra <= 'Z')
    if not(minuscula or mayuscula):
        mensajedescifrado += letra
    else:
        ascii = ord(letra)
        baseAscii = ord('a')
        if mayuscula:
            baseAscii = ord('A')
        nuevoAscii = (ascii - baseAscii - veces) % 26 + baseAscii
        nuevaLetra = chr(nuevoAscii)
        mensajedescifrado += nuevaLetra

print ("El mensaje descifrado es:")
print(mensajedescifrado)