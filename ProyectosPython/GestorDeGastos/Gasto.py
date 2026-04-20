class Gasto:
    def __init__(self, gasto, monto):
        self.gasto=gasto
        self.monto=monto

    def __str__(self):
        return f"{self.gasto} - {self.monto}"