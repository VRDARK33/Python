"""
🐍 Ejercicio del día — Día 6
Nivel: Intermedio
Tema: Recursión

Suma de dígitos
Crea una función recursiva suma_digitos(n) que reciba un número entero positivo y retorne la suma de todos sus dígitos. 
Sin convertir a string, solo con matemáticas.
suma_digitos(1234)  # 10  → 1+2+3+4
suma_digitos(9999)  # 36  → 9+9+9+9
suma_digitos(105)   # 6   → 1+0+5
suma_digitos(7)     # 7   → caso base

Pista matemática
Para extraer dígitos sin strings tienes dos operadores clave:
python
1234 % 10    # 4  → último dígito
1234 // 10   # 123 → número sin el último dígito
Piensa así: en cada llamada recursiva tomas el último dígito y llamas a la función con el resto del número.

Reglas:

Función estrictamente recursiva — sin for, sin while
Sin convertir a string con str()
Identifica bien el caso base: ¿cuándo un número no necesita seguir dividiéndose?

Pista del caso base: ¿Qué pasa cuando el número es menor que 10? Ya es un solo dígito — no hay nada más que sumar.
"""

def suma_digitos(n):
    if n < 10:
        return n

    return (n % 10) + suma_digitos(n // 10)

numero = 1234

reultado = suma_digitos(numero)

print(reultado)