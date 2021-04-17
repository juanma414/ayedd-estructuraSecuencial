impBruto = float(input("ingrese el importe bruto:"))
descuento = impBruto * 0.04
impBonif = impBruto - descuento
iva = impBonif * 0.21
impNeto = impBonif + iva
print("el importe bruto es:",impBruto)
print("la bonificación del 4% es:",descuento)
print("el importe bruto bonificado es:",impBonif)
print("el IVA es:",iva)
print("el importe neto resultante es:",impNeto)
