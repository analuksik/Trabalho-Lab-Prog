import math
try:
  r = float(input("Digite o valor do raio (r): "))
  if r < 1:
    print(f"Valor inválido! O raio deve ser maior que zero.")
  else:
    area = 4 * math.pi * (r**2)
    print(f"O valor da área da esfera de raio {r} é de: {area:.2f}")
    volume = 4/3 * math.pi * (r**3)
    print(f"O valor do volume da esfera de raio {r} é de: {volume:.2f}")
except:
  print("ERRO DE EXCEÇÂO")
