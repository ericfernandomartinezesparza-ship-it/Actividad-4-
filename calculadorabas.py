while True:
    print("\n1. Sumar")
    print("2. Restar")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "3":
        break

    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))

    if opcion == "1":
        print("Resultado:", a + b)
    elif opcion == "2":
        print("Resultado:", a - b)
    else:
        print("Opción no válida")
