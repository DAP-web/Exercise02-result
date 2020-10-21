from Cuenta import Finanzas
from Ingreso import Ingreso
from Egreso import Egreso

print("Usted ha abierto su cuenta con un saldo inicial de $0.00")
RIngreso = Ingreso()
RCuenta = Finanzas()
REgreso = Egreso()

while True:
    Menu = """\nElija una de las siguientes opciones:
    0-Salir de la app
    1-Registrar un ingreso
    2-Registrar un egreso
    3-Recuperar el total de ingresos
    4-Recuperar el total de egresos
    5-Solicitar un reporte de transacciones (ingresos y egresos)
    6-Recuperar el total de la cuenta\n"""
    print(Menu)
    opcion = int(input("Ingrese una de las opciones brindadas: "))
    if opcion==0:
        break
    elif opcion==1:
        ingreso = round(float(input("¿Cuál es la cantidad que desea ingresar a la cuenta?")),2)
        RCuenta.ingreso(RIngreso.registrarIngreso(ingreso))

    elif opcion==2:
        egreso = round(float(input("¿Cuál es la cantidad que desea retirar de la cuenta?")),2)
        RCuenta.egreso(REgreso.registrarEgreso(egreso))
    elif opcion==3:
        mensaje = RIngreso.ingresos
        print(f"Su total de ingresos es de ${mensaje}.")
    elif opcion==4:
        mensaje2 = REgreso.egresos
        print(f"Su total de egresos han sido de ${mensaje2}")
    elif opcion==5:
        reporteI = RIngreso.ingresos
        reporteE = REgreso.egresos
        print("-"*100)
        reporte = f"""Reporte de transacciones:
        Ingresos: ${reporteI}
        Egresos: ${reporteE}"""
        print(reporte)
        print("-"*100)
    elif opcion==6:
        reporteC = round(RCuenta.cuenta,2)
        print(f"Su saldo en cuenta es de ${reporteC}.")
    else:
        print("No ha seleccionado ninguna opción válida. Por favor ingrese únicamente una de las opciones brindadas")