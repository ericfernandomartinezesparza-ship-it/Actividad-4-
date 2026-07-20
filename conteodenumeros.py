mayores = 0
menores = 0
ceros = 0

cantidad = int(input("¿Cuántos números vas a ingresar?: "))

for i in range(cantidad):
    numero = float(input("Número: "))

    if numero > 0:
        mayores += 1
    elif numero < 0:
        menores += 1
    else:
        ceros += 1

print("Mayores que cero:", mayores)
print("Menores que cero:", menores)
print("Iguales a cero:", ceros)
