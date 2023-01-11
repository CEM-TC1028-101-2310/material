
compras_anteriores = int(input("Ingrese el número de compras anteriores: "))
monto_actual = float(input("Ingrese el monto de la compra actual: "))

descuento = 0
if compras_anteriores >= 5 and compras_anteriores <= 10:
    descuento = descuento + 0.05
    # descuento += 0.05
elif compras_anteriores >= 11 and compras_anteriores <= 20:
    descuento += 0.07
elif compras_anteriores > 20:
    descuento += 0.1
    
if monto_actual < 2000:
    descuento += 0
elif monto_actual <= 5000:
    descuento += 0.03
elif monto_actual <= 8000:
    descuento += 0.05
else:
    descuento += 0.07
    
total = monto_actual - (monto_actual * descuento)
# total = monto_actual * (1 - descuento)

print(f"El total a pagar es de: ${total:,.2f}")