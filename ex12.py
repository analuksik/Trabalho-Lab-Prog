massa = float(input("Digite seu peso (kg): "))
h = float(input("Digite sua altura (m): "))
imc = massa / (h **2)
print(f"Seu IMC é de: {imc:.2f}")
if imc <= 18.5:
  print("Classificação: Magreza")
elif imc < 25:
  print("Classificação: Saudável")
elif imc < 30:
  print("Classificação: Sobrepeso")
elif imc < 35:
  print("Classificação: Obesidade Grau I")
elif imc < 40:
  print("Classificação: Obesidade Grau II (Severa)")
else:
  print("Classificação: Obesidade Grau III (Morbida)")
