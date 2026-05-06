for i in range(5):
    print(i)

#for recorre cada elemento de una lista
frutas = ["mango", "banano","manzana"]

for fruta in frutas:
    print(fruta)

#range() genera numeros : range(5) -> 0 1 2 3 4
for numero in range(1,6):
    print(numero)

#combinar con condicionales
numeros = [1,2,3,4,5,6,7,8]
for numero in numeros:
    if numero % 2 == 0:
        print(f"es par {numero}")
