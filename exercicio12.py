from datetime import date

ano = int(input("Digite o ano de nascimento: "))
ano_atual = date.today().year
idade = ano_atual - ano

if idade >= 16:
    print(f"Você tem {idade} anos, portanto já pode votar")
elif idade > 110:
    print("Idade inválida")
else:
    print(f"Você tem {idade} anos, portanto não pode votar")