temperatura = int(input("Digite a temperatura em °C: "))

if temperatura < 13:
    print("Clima frio.")
elif temperatura <= 22:
    print("Clima agradável.")
else:
    print("Clima quente.")