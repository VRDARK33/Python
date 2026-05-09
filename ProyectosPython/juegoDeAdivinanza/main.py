"""
1.
El programa elige un número aleatorio entre 1 y 100 con
random.randint(1, 100)
2.
El usuario tiene 7 intentos para adivinar
3.
Cada intento le dice si es muy alto, muy bajo o correcto
4.
Al terminar muestra cuántos intentos usó
5.
Pregunta si quiere jugar de nuevo
"""

import random

numero = random.randint(1, 100)

print(numero)



intentos_restantes = 7
intentos_usados = 0

while True:
    respuesta = int(input("adivine el numero secreto: "))

    if respuesta > numero:
        print("Es muy alto")
        intentos_usados += 1
        intentos_restantes -= 1
    elif respuesta < numero:
        print("Es muy bajo ")
        intentos_usados += 1
        intentos_restantes -= 1
    else:
        print(f"Es el numero correcto {respuesta} - numero secreto: {numero}")
        print(f"intentos usados = {intentos_usados} - intentos sobrantes = {intentos_restantes}")
        volver_a_jugar = input("quieres volver a jugar [si/no]: ").lower()
        if volver_a_jugar == "si":
            numero = random.randint(1, 100)
            print(numero)
            intentos_restantes = 7
            intentos_usados = 0
        else:
            print("adios...")
            break

    if intentos_usados == 7:
        print("perdiste...")
        volver_a_jugar = input("quieres volver a jugar [si/no]: ").lower()
        if volver_a_jugar == "si":
            numero = random.randint(1, 100)
            print(numero)
            intentos_restantes = 7
            intentos_usados = 0
        else:
            print("adios...")
            break