class Egreso:
    def __init__(self):
        self.egresos=0.00

    def registrarEgreso(self,egreso):
        self.egresos+=egreso
        return egreso