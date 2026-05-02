# Ejemplo de un diccionario
persona = {
    "nombre" : "Brayan",
    "edad" : 25,
    "ciudad": "Pereira"
}

# Forma de acceder
print(persona["nombre"])

# Forma de modificar
persona["edad"] = 28
print(persona["edad"])

# Recorrer un diccionario 
for clave, valor in persona.items():
    print(clave, valor)