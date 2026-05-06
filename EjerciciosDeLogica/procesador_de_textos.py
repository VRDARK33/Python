"""
Tienes esta lista de frases:
pythonfrases = [
    "  Python es increíble  ",
    "LA PROGRAMACIÓN ES DIVERTIDA",
    "hola mundo",
    "  aprender cada día   ",
    "EL CÓDIGO ES ARTE"
]
Crea una función procesar_frases(frases) que en una sola línea con list comprehension limpie y 
transforme cada frase aplicando todo esto a la vez:

Eliminar espacios al inicio y al final
Convertir a formato título (primera letra de cada palabra en mayúscula)
Filtrar las frases que tengan menos de 12 caracteres después de limpiarlas

La salida debe ser:
Frases procesadas:
- Python Es Increíble
- La Programación Es Divertida
- Aprender Cada Día
- El Código Es Arte
Nota: "hola mundo" tiene 10 caracteres después de limpiarla, así que se filtra y no aparece.

Reglas:

El procesamiento debe hacerse en una sola list comprehension
Usa los métodos .strip(), .title()
Usa len() para el filtro dentro de la comprehension

Pista: Una list comprehension puede tener transformación y filtro al mismo tiempo:
python[expresion for elemento in lista if condicion]
El truco está en que la condicion debe evaluar el texto ya limpio, no el original.
"""

pythonfrases = [
    "  Python es increíble  ",
    "LA PROGRAMACIÓN ES DIVERTIDA",
    "hola mundo",
    "  aprender cada día   ",
    "EL CÓDIGO ES ARTE"
]


def procesar_frases(frases):
    frases_procesadas = [frase.strip().title() for frase in frases if len(frase.strip()) >= 12]

    print("Frases procesadas.")

    for frase in frases_procesadas:
        print(f"- {frase}")

procesar_frases(pythonfrases)

