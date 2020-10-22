class Cuenta:
    def __init__(self):
        self.cuenta = 0.00
        
    def ingreso(self,ingreso):
        self.cuenta+=ingreso
        print(f"\nHas registrado un ingreso de ${ingreso:.2f}.")
        print(f"\nTu saldo en cuenta es de ${self.cuenta:.2f}.")
        
    def egreso(self,egreso):
        self.cuenta-=egreso
        print(f"\nHas retirado ${egreso:.2f}.")
        print(f"\nTu saldo en cuenta es de ${self.cuenta:.2f}")
        