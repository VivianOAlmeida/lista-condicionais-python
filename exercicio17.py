tipo = input("Tipo (R-residencial, C-comercial, I-industrial): ").upper()
consumo = float(input("Consumo em kWh: "))

if tipo == "R":
    if consumo >= 500:
        valor = consumo * 0.60
    else:
        valor = consumo * 0.75
elif tipo == "C":
    if consumo >= 1000:
        valor = consumo * 0.80
    else:
        valor = consumo * 0.95
elif tipo == "I":
    if consumo >= 5000:
        valor = consumo * 1.00
    else:
        valor = consumo * 1.15
else:
    print("Tipo inválido")
    valor = 0

print("Valor a pagar: R$", valor)