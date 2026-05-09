contador = 1;

while contador <= 5:
    print(contador)
    contador += 1

#while repite mientras una condicion sea TRUE
contador = 1 

while contador <= 5:
    print(f"contador {contador}")
    contador += 1 # sin esta linea es bucle infinito

#break: salir del bucle antes de tiempo
while True:
    respuesta = input("escriba salir para terminar el bucle: ").lower()

    if respuesta == "salir":
        break

    print(f"tu respuesta {respuesta}")

#contiue: saltar esta vuelta y seguir

for i in range(1,6):
    if i == 3:
        continue
    print(i)