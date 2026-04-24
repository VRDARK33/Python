#Ejercicio 1 Crea una función que reciba un número y diga si es par o impar

def par_or_impar(num):
    if num % 2 == 0:
        return "par"
    else:
        return "impar"    


resultado = par_or_impar(7)
print(f"El numero es {resultado}")

#Ejercicio 2 Crea una función que reciba una lista y devuelva la suma total

def sum_list(lista):
    resultado = 0
    for num in lista:
        resultado += num
    
    return resultado

numero = [1,2,3,4,5]
total = sum_list(numero)
print(f"el valor total de la lista es: {total}")


"""
Ejercicio 3 (importante)

Crea una función que reciba una lista y devuelva:

el número mayor
el número menor

👉 usando lo que aprendiste
"""

def num_mayor_and_menor_list(lista):
    maxx = lista[0]
    minn = lista[0]

    for num in lista:

        if num > maxx:
            maxx = num
        if num < minn:
            minn = num
    return maxx,minn


mayor, menor = num_mayor_and_menor_list(numero)    

print(f"mayor: {mayor}")
print(f"menor: {menor}")