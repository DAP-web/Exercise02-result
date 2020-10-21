class Ingreso:
    def __init__(self):
        self.ingresos = 0.00

    def registrarIngreso(self,ingreso):
        self.ingresos+=ingreso
        return ingreso