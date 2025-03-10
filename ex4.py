try:
  h = float(input("Digite a sua altura: "))
  s = str(input("Digite seu sexo masculino (h) ou feminino (m): "))
  if s == 'h':
    pIdeal = (72.7 * h) - 58
  elif s == 'm':
    pIdeal = (62.1 * h) - 44.7
    print(f"O seu peso ideal é de: {pIdeal:.2f}")
  else:
    print("ERRO: DADOS DE ENTRADA")
except:
  print("ERRO: ERRO DE EXCEÇÃO")
