salario = float(input("Salário: "))
parcela = float(input("Parcela: "))

if parcela <= salario * 0.3:
    print("Aprovado")
else:
    print("Negado")