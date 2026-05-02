from gestor import  Gestor


gestor = Gestor()
def menu():
    while True:
        print("Bienvenido al gestor de gastos \n")
        try:
            opcion = int(input(" 1.Agregar gasto\n 2.listar gastos\n 3.Gastos totales\n 4.salir : "))
        except ValueError:
            print("debes ingresar un numero \n")
            continue

    
        match opcion:
            case 1:
                while True:
                    gasto  = input("ingrese el nombre del gasto: ")
                    try:
                        monto = float(input("ingrese el valor del monto: "))
                    except ValueError:
                        print("ingrese un numero valido.")    

                    gestor.agregar_gasto(gasto, monto)

                    seleccion = str.lower(input("desea ingresar otro gasto[si/no]: "))

                    if seleccion != "si":
                        print("Regresando al menu...")
                        print("\n")
                        break
 
            case 2:
                gestor.listar_gastos()
                print("\n")
            case 3:
                gestor.calcular_total()   
                print("\n")
            case 4:
                print("saliendo...")
                break   
            case _:
                print("opcion no valida")

print("\n")
menu()
    
 