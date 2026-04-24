from gasto import Gasto

class Gestor: 
    def __init__(self):
        self.gastos = []

    def agregar_gasto(self, gasto,monto):
        g = Gasto(gasto,monto)
        self.gastos.append(g)
    
    def listar_gastos(self):

        for i in self.gastos:
            print(i)


    def calcular_total(self):
        total = 0
        for i in self.gastos:
            total += i.monto

        print("El total de gastos es: ", total)




