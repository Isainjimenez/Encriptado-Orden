import pyfiglet

def banner():
    ascii_banner = pyfiglet.figlet_format("ORDEN")
    print(ascii_banner)

# Corrige las comillas en el enlace al proyecto
print("OPEN-SOURCE PROJECT | https://github.com/Saulo-lopezSu/metodos_de_encriptacion")
print("by Saulo Gonzalez L.")

alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789_"
clave = "rcipto".upper()

def encriptar(filas, mensaje, clave):
    posiciones = [alfabeto.find(c) for c in clave]
    orden = [0] * len(clave)
    matriz = []
    index = 0
    encriptado = ""

    for i in range(len(posiciones)):
        maximo = max(posiciones)
        if i == 0:
            orden[len(clave) - 1] = posiciones.index(maximo)
        else:
            minimo = min(posiciones)
            orden[i - 1] = posiciones.index(minimo)
            posiciones[posiciones.index(minimo)] = maximo

    for i in range(len(mensaje)):
        matriz.append([])
        for j in range(len(clave)):
            if index >= len(mensaje):
                matriz[i].append('X')
            else:
                matriz[i].append(mensaje[index])
                index += 1

    # Imprime la matriz (opcional)
    for fila in matriz:
        print(" ".join(fila))

    for i in orden:
        for j in range(filas):
            encriptado += matriz[j][i]

    print(f"Filas: {filas}, Columnas: {len(mensaje)}, Mensaje encriptado: {encriptado}")
    return encriptado

def descifrar(filas, mensaje, clave):
    orden = [clave.find(c) for c in nuevaClave]
    matriz = []
    nuevaClave = ""
    descifrado = ""
    index = 0

    for i in range(len(clave)):
        posiciones.append(alfabeto.find(clave[i]))
        posicionesaux.append(alfabeto.find(clave[i]))

    # Resto del código de descifrado (no incluido aquí para brevedad)

# Ejemplo de uso
encriptar(4, "la clave secreta".upper(), clave)
# descifrar(4, "AEEX  TXACXXCSAXLVRXLEXX".upper(), clave)  # Completa esta función


