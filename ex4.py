try:
  h = float(input("Digite a sua altura: "))
  s = str(input("Digite seu sexo (h) ou (m): "))
  if s != 'h' and s != 'm':
    print(f"Dados de entrada inválidos!")
  elif s == 'h':
    pIdeal = (72.7 * h) - 58
  else:
    pIdeal = (62.1 * h) - 44.7
  print(f"O seu peso ideal é de: {pIdeal:.2f}")
except:
  print("ERRO: ERRO DE EXCEÇÃO")
