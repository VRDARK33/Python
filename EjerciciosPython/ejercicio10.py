"""
1.
Crea un juego: el programa elige el número 7 (fijo por ahora)
2.
El usuario adivina con input() en un bucle while
3.
Si adivina: muestra "¡Correcto!" y termina con break
4.
Si no: muestra "Muy alto" o "Muy bajo" según corresponda
Meta del día: saber que for se usa cuando sabes cuántas veces repetir, y while cuando repites hasta que algo cambie.
"""

numero = 7

while True:
    respuesta = int(input("adivina el numero secreto: "))

    if respuesta == numero:
        print("Correcto")
        break
    elif respuesta > numero:
        print("Muy alto")
        continue
    elif respuesta < numero:
        print("Muy bajo")
        continue