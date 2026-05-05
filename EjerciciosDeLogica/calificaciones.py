"""
Nivel: Intermedio
Tema: Diccionarios + Funciones

Sistema de calificaciones
Tienes una lista de estudiantes con sus notas:
Crea una función generar_reporte(estudiantes) que recorra el diccionario y para 
cada estudiante calcule su promedio e imprima su estado:
📊 REPORTE DE CALIFICACIONES
------------------------------
Ana     | Promedio: 86.6 | Aprobado ✅
Carlos  | Promedio: 61.6 | Aprobado ✅
Maria   | Promedio: 96.4 | Aprobado ✅
Pedro   | Promedio: 73.0 | Aprobado ✅
Luis    | Promedio: 48.0 | Reprobado ❌
------------------------------
Mejor estudiante: Maria (96.4)
Peor estudiante:  Luis  (48.0)
Reglas de aprobación: promedio >= 60 aprueba, menor de 60 reprueba.

Reglas:

No uses max() ni min() directamente sobre el diccionario — calcúlalos tú comparando promedios
Usa sum() y len() para el promedio
Redondea a 1 decimal con round(numero, 1)

Pista: Guarda el mejor y peor estudiante con variables mejor_nombre, 
mejor_promedio mientras recorres el diccionario. 
Compara el promedio de cada estudiante contra el guardado y actualiza si corresponde.
"""

estudiantes = {
    "Ana":    [85, 92, 78, 90, 88],
    "Carlos": [60, 55, 70, 65, 58],
    "Maria":  [95, 98, 100, 92, 97],
    "Pedro":  [70, 75, 68, 80, 72],
    "Luis":   [40, 55, 48, 52, 45]
}

def generar_reporte(estudiantes):
    mejor_estudiante, peor_estudiante = None, None
    mejor_promedio, peor_promedio = 0, 101

    for nombre , notas in estudiantes.items():
        promedio = sum(notas) / len(notas) 
        estado = "Aprobado" if resultado >=60 else "Reprobado"
        print(f"{nombre} | Promedio: {promedio } | {estado}")

        if resultado > mejor_promedio:
            mejor_estudiante, mejor_promedio = nombre, promedio 
        
        if resultado < peor_promedio:
            peor_estudiante, peor_promedio = nombre, promedio 
            
            
    print(f"Mejor estudiante: {mejor_estudiante} ({mejor_promedio})")
    print(f"Peor estudiante: {peor_estudiante} ({peor_promedio})")
        

generar_reporte(estudiantes)