try:
  n1 = float(input("Digite o 1º número: "))
  n2 = float(input("Digite o 2º número: "))
  if n1 == n2:
    print("Os números devem ser distintos! ")
  else:
    n3 = float(input("Digite o 3º número: "))
    if n1 == n3 or n2 == n3:
      print("Os números devem ser distintos! ")
  if n1 > n2 and n1 > n3:
      maior = n1
      segundo_maior = max(n2, n3)
  elif n2 > n1 and n2 > n3:
      maior = n2
      segundo_maior = max(n1, n3)
  else:
      maior = n3
      segundo_maior = max(n1, n2)

  media = (maior + segundo_maior) / 2
  print(f"A média dos dois maiores números é: {media} ")
except Exception as ERRO_EXECAO:
  print(f"ERRO DE EXCEÇÃO: {ERRO_EXECAO}")
