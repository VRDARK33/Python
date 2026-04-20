from Gasto import *

class Gestor: 
    def __init__(self):
        self.gastos = []

    def ingresarGasto(self):
        while True:
            gasto = str(input("Ingrese el nombre del gasto: "))
            monto = float(input("Ingrese el valor del gasto: "))

            g = Gasto(gasto, monto)

            self.gastos.append(g)

            print("Gasto ingresado correctamente")

            seleccion = str.lower(input("Desea ingresar otro gasto (SI/NO): "))

            if seleccion != "si":
                print("adios...")
                break
    
    def listaGastos(self):

        for i in self.gastos:
            print(i)


    def GastosTotales(self):
        total = 0
        for i in self.gastos:
            total += i.monto

        print("El total de gastos es: ", total)




