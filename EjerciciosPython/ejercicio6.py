"""
Ejercicio 1

Crea un diccionario con:

nombre
edad
país

Y muéstralo
"""

persona = {
    "Nombre" : "brayan",
    "Edad" : 25,
    "pais" : "colombia"
}

for clave, valor in persona.items():
    print(clave, valor)

"""
Ejercicio 2

Pide datos al usuario y guárdalos en un diccionario
"""

diccionario = {
    "Nombre" : input("Ingresa tu nombre "),
    "Edad" : int(input("Ingrese su edad ")),
    "Pais" : input("Ingrese su pais de origen ")
}

"""
Ejercicio 3 (nivel real)

Crea un programa que:

Permita agregar varias personas (nombre y edad)
Las guarde en una lista de diccionarios
Muestre todas las personas

"""

lista_de_personas = []

while True:
    nombre = input("Ingrese el nombre ")
    while True:
        try:
            edad = int(input("Ingrese su edad "))
            break
        except:
            print("Edad invalida. intente de nuevo")
    
    lista_de_personas.append({
        "Nombre" : nombre,
        "edad" : edad
    })

    seleccion = input("Desea ingresar otra persona [si/no]: ").lower()

    if seleccion != "si":
        print("Adios...")
        break


print("Listas de personas")

for persona in lista_de_personas:
    print(f"Nombre {persona["Nombre"]} - Edad: {persona["edad"]}")