#ejercicio1 Imprime los números del 1 al 10 usando while

contador = 1

while contador <= 10:
    print(contador)
    contador += 1   

#ejercicio2 Pide una contraseña hasta que sea correcta

contraseña = 1234

while True:
    pedir = int(input("ingrese la contraseña: "))

    if pedir == contraseña:
        print("acceso permitido")
        break
    else:
        print("contraseña incorrecta")


#ejercciio3 Pide 5 números y muestra la suma total
 
resultado = 0
numero = 0

for i in range(5):
    numero = int(input(f"ingrese un numero {i+1}: "))
    resultado += numero

print(f"el resultado total es: {resultado}")