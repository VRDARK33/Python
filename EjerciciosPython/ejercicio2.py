# pide al usuario nombre y edad y imprime

nombre = input("ingrese su nombre: ")
edad = int(input("ingrese su edad: "))

print(f"hola {nombre}, tienes {edad} años")


# pide un numero y muestra si es positivo, negativo o si es cero

numero = int(input("ingrese un numero: "))

if numero > 0:
    print("el numero es positivo")
elif numero < 0:
    print("el numero es negativo")
else:
    print("el numero es 0")


numero1 = int(input("ingrese un numero: "))
numero2 = int(input("ingrese otro numero: "))

if numero1 >  numero2:
    print(f"el numero {numero1} es mayor que {numero2}")
elif numero1 < numero2    :
    print(f"el numero {numero2} es mayor que {numero1}")
else:
    print("los numeros son iguales ")