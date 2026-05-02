
lista_de_personas = []


def agregar_persona(nombre, edad):
    lista_de_personas.append({
        "Nombre" : nombre,
        "Edad" : edad
    })

def listar_personas(lista):
    for persona in lista:
        print(f"Nombre: {persona['Nombre']} - Edad: {persona['Edad']}")

def buscar_persona(nombre, lista):
    encontrado = False
    for i in lista:
        if nombre == i["Nombre"]:
            print(f"Nombre: {i["Nombre"]} - Edad: {i["Edad"]}")
            encontrado = True

    if not encontrado:
        print("Persona no encontrada")




def menu():
    while True:
        print("Bienvenido al sistema de personas \n")

        try:
            opcion = int(input(" 1.Agregar persona\n 2.Mostrar personas\n 3.Buscar persona por nombre\n 4.Salir : "))
        except ValueError:
            print("Debe ingresar un numero valido")
            continue

        match opcion:
            case 1: 
                while True:
                    nombre = input("Ingrese el nombre de la persona: ").lower()
                    try:
                        edad = int(input("ingrese la edad de la persona: "))
                    except ValueError:
                        print("debe ser un numero valido: ")
                        continue

                    agregar_persona(nombre,edad)

                    desicion = input("Desea ingresar otra persona [si/no]: ").lower()

                    if desicion != "si":
                        print("Volviendo al menu... \n")
                        break
            case 2:
                lista_personas = lista_de_personas
                listar_personas(lista_personas)
            
            case 3:
                lista_personas = lista_de_personas
                nombre = input("Ingrese el nombre de la persona: ").lower()
                buscar_persona(nombre, lista_personas)

                    
menu()


