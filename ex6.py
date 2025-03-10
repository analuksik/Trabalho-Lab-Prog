try:
  num = float(input("Digite um número positivo: "))
  if num < 0:
    print("O número deve ser positivo!")
  quadrado = num ** 2
  if quadrado % 2 != 0:
    print(f"O número {num} é ímpar!")
  else:
    print(f"O número {num} não é ímpar!")
  if quadrado % 11 ==  0:
    print(f"O número {num} é múltiplo de 11!")
  else:
    print(f"O número {num} não é múltiplo de 11!")
except:
  print("ERRO: ERRO DE EXCEÇÃO")
