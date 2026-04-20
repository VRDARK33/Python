from Gestor import * 

def menu():
    gestor = Gestor()
    while True:
        print("Bienvenido al gestor de gastos \n")
        opcion = int(input(" 1.Agregar gasto\n 2.listar gastos\n 3.Gastos totales\n 4.salir : "))

    
        match opcion:
            case 1:
                gestor.ingresarGasto()
            case 2:
                gestor.listaGastos()
            case 3:
                gestor.GastosTotales()   
            case 4:
                print("saliendo...")
                break   
            case _:
                print("opcion no valida")


menu()
    
 