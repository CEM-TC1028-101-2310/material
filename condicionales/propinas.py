
total = float(input("Ingrese el total de la cuenta: "))
personas = int(input("Ingrese el número de personas: "))

por_persona = total / personas

if por_persona < 150:
    pago = por_persona * 1.1
    porcentaje = 10
elif por_persona <= 250:
    pago = por_persona * 1.13
    porcentaje = 13
else:
    pago = por_persona * 1.15
    porcentaje = 15
    
print(f"Cada persona debe pagar ${pago:,.2f} que incluye {porcentaje}% de propina.")
    
# Cada persona debe pagar $16.20 que incluye 10% de propina.