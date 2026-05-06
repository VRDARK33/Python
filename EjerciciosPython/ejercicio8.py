"""
1.
Pídele al usuario su edad y si tiene licencia (responde "si" o "no")
2.
Solo puede alquilar un carro si tiene más de 18 años Y tiene licencia
3.
Muestra un mensaje claro según cada caso posible
"""

edad = int(input("Ingrese su edad: "))
licencia = input("Cuenta con licencia[si/no]: ").lower()

if edad > 18 and licencia == "si":
    print("puedes alquilar el coche")
elif edad <= 18:
    print("No eres mayor de 18")
else:
    print("No cuentas con licencia")