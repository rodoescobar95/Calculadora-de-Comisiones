nombre = input("Dime tu nombre ")
ventas = input("monto de venta mensual $")
ventas = float(ventas)
comision = ventas * 13 / 100
comision = round(comision,2)
print(f"Excelente {nombre}, tus comisiones este mes son de ${comision}")