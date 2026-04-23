# ejercicio1 Crea una lista con 5 números y muéstralos con un for

numeros = [1,2,3,4,5]

for numero in numeros:
    print(numero)

#ejercicio2 Pide 5 números al usuario y guárdalos en una lista

numeros = []
i = 1

while i <= 5:
    numero = int(input(f"ingrese el valor #{i}: "))
    numeros.append(numero)
    i += 1

print(numeros)

"""
Ejercicio 3 (importante)

Muestra:

el número mayor
el número menor

👉 NO uses max() ni min()
👉 Hazlo con lógica (esto es tipo entrevista)
"""

if len(numeros) == 0:
    print("lista vacia")
else:
    maxx = numeros[0]
    minn = numeros[0]

    for numero in numeros:

        if numero > maxx:
            maxx = numero

        if numero < minn:
            minn = numero 




print(maxx)
print(minn)