#una funcion es una forma de reutilizar codigo

#forma de estrutura de una funcion sin parametros y con una impresion por consola

def saludar():
    print("hola")

saludar()

#estrutura de funcion con parametros en este caso recibe un parametro llamado nombre

def saludo2(nombre):
    print(f"hola, {nombre}")

saludo2("brayan")

#estrutura de funcion cono retorno

def suma(a,b):
    return a + b

resultado = suma(3,4)
print(resultado)

