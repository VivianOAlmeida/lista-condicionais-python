numero1 = float(input("Insira o 1° número: "))
numero2 = float(input("Insira o 2° número: "))
numero3 = float(input("Insira o 3° número: "))

if numero1 > numero2 and numero1 > numero3:
    print("O 1° numero é maior.")
elif numero2 > numero1 and numero2 > numero3:
    print("O 2° número é maior.")
elif numero1 == numero2 == numero3:
    print("Os três números são iguais.")
else:
    print("O 3° número é maior.")