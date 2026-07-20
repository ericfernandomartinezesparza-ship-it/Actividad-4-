vocales = 0
consonantes = 0

while True:
    letra = input("Ingresa una letra (espacio para terminar): ")

    if letra == " ":
        break

    letra = letra.lower()

    if letra in "aeiou":
        vocales += 1
    elif letra.isalpha():
        consonantes += 1

print("Vocales:", vocales)
print("Consonantes:", consonantes)
