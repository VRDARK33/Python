"""
Tu primer ejercicio (obligatorio)

Haz un programa que:

1.Pida el nombre
2. Pida la edad
3. Si tiene 18 o más → diga "Puedes entrar"
4. Si no → diga "No puedes entrar"
"""

nombre = input("ingrese su nombre : ")

edad = int(input("ingrese su edad: "))

print(f"hola {nombre}")
if edad >= 18:
    print("Puedes entrar")
else:
    print("No puedes entrar")


nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
ciudad = input("Ingrese su  ciudad: ")

print(f"Hola, soy {nombre} tengo {edad} años y vivo en {ciudad}")

