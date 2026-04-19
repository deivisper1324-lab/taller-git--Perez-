# --- SECCION DE ENTRADA ---
tipo_moneda = int(input("Tipo de Moneda (1: Bs, 2: $): ")) 
monto = int(input("monto a retirar: "))
tipo_cuenta = int(input("Tipo de Cuenta (1: Ahorro, 2: Corriente): "))
# --- SECCION DE VALIDACIONES ---

# 1. Validar que sea multiplo de 10 
if monto % 10 != 0:
    print("Error: Monto no compatible con denominaciones disponibles") 
    exit()  
# 2. Validar limites de seguridad segun la moneda 
if tipo_moneda == 1: 
    if monto > 10000:
     print("Transacción denegada: Excede limite diario")
     exit()
elif tipo_moneda == 2: 
    if monto > 500:
        print("Transacción denegada: Excede limite diario")
        exit()
else:
    print("Error: Tipo de moneda no valido")
    exit()

    # --- CALCULOS DE COMISION ---
comision = 0
if tipo_cuenta == 2: 
    comision = monto * 0.05

total_debitar = monto + comision 
# --- CALCULO DE DESGLOSE DE BILLETES ---
cant_100 = monto // 100
resto = monto % 100

cant_50 = resto // 50
resto = resto % 50

cant_20 = resto // 20
resto = resto % 20

cant_10 = resto // 10
# --- SECCION DE SALIDA ---
nombre_moneda = "Bs" if tipo_moneda == 1 else "$"

print("-" * 30)
print(f"RESUMEN DE RETIRO EN {nombre_moneda}")
print(f"Billetes de 100: {cant_100}")
print(f"Billetes de 50: {cant_50}")
print(f"Billetes de 20: {cant_20}")
print(f"Billetes de 10: {cant_10}")
print(f"Total debitado: {total_debitar} {nombre_moneda}")
print ("-" * 30)


