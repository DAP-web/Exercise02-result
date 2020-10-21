class Finanzas:
    def __init__(self):
        self.cuenta = 0.00
        
    def ingreso(self,ingreso):
        self.cuenta+=ingreso
        print(f"Has registrado un ingreso de ${ingreso}.")
        print(f"Tu saldo en cuenta es de ${self.cuenta}.")
        
    def egreso(self,egreso):
        self.cuenta-=egreso
        print(f"Has retirado ${egreso}.")
        print(f"Tu saldo en cuenta es de ${self.cuenta:.2f}")
        