# Manejo de errores

try: 
    numero = int(input("Ingrese un numero: "))
except ValueError:
    print("Entrada invalida")