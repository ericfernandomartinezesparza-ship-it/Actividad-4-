import random

numero = random.randint(1,100)

while True:
    intento = int(input("Adivina el número (1-100): "))

    if intento == numero:
        print("¡Correcto!")
        break
    elif intento < numero:
        print("Muy bajo")
    else:
        print("Muy alto")
