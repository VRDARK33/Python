"""
1.
Pídele al usuario una nota entre 0 y 100
2.
Imprime: "Excelente" si es ≥ 90, "Bueno" si es ≥ 70, "Aprobado" si es ≥ 60, 
"Reprobado" si es menor
3.
Extra: si el usuario ingresa un número fuera de 0-100, muestra "Nota inválida"
"""

nota = int(input("Ingrese una nota entre 0 - 100: "))

if nota < 0 or nota >= 101:
    print("Nota invalida")
elif nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Bueno")
elif nota >= 60:
    print("Aprobado")
elif nota < 60:
    print("Reprobado")
