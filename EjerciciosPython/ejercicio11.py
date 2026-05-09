"""
1.
Crea una lista vacía llamada
aprobados
2.
Con un while, pídele notas al usuario hasta que escriba -1
3.
Si la nota es ≥ 60, agrégala a
aprobados
4.
Al final, imprime cuántos aprobaron y cuál fue el promedio

"""

aprobados = []

while True:
    try:
        nota = int(input("ingrese un nota: "))
        if nota >= 60:
            aprobados.append(nota)
    except ValueError:
        print("no es un dato valido")
    
    respuesta = int(input("si no desea ingresar mas notas presione -1: "))

    if respuesta == -1:
        print("saliendo...")
        break

promedio = sum(aprobados) / len(aprobados)

print(f"aprobaron {len(aprobados)} y el promedio fue {promedio}")