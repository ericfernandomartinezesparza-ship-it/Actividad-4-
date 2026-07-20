contador = 0
numero = 1

while numero <= 100:
    if numero % 2 != 0:
        contador += 1
    numero += 1

print("Cantidad de números impares:", contador)
