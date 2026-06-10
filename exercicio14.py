
idade = int(input("Digite sua idade: "))

if idade >= 0 and idade <= 11:
    print("Você é uma criança")
elif idade >=12 and idade <= 17:
    print("Você é um adolescente")
else:
    print("Você é um adulto")