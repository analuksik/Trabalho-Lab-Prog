try:
  valor = float(input("Digite o valor: "))
  esp = str(input("O valor foi digitado em Dólar, Libra ou em Real? "))
  if valor < 0:
    print("ERRO: o valor deve ser positivo")
  elif esp == 'real':
    print(f"{valor} Reais equivale a {(valor * 5.84):.2f} Dólares e {(valor * 7.54):.2f} Libras")
  elif esp == 'dolar':
    print(f"{valor} Dólares equivale a {(valor * 0.77):.2f} Libras e {(valor * 5.88):.2f} Reais ")
  elif esp == 'libra':
    print(f"{valor} Libras equivale a {(valor * 4.08):.2f} Reais e {(valor * 1.12):.2f} Dólares")
  else:
    print("ERRO: DADOS DE ENTRADA")
except:
  print("ERRO: ERRO DE EXCEÇÃO")
