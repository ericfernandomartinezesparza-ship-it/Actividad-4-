inicio = int(input("Número inicial: "))
diferencia = int(input("Diferencia: "))
cantidad = int(input("Cantidad de términos: "))

contador = 0
actual = inicio

while contador < cantidad:
    print(actual)
    actual += diferencia
    contador += 1
