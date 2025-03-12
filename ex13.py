try:
  n1 = float(input("Digite o 1° número real:"))
  n2 = float(input("Digite o 2° número real:"))
  n3 = float(input("Digite o 3° número real:"))
  media = (n1  + n2 + n3) / 3
  if media < 10 and media > 200:
    print(f"O Cubo da média dos tres números é de: {(media ** 3):.5f}")
  else:
    print(f"A média dos três números é: {media} ")
  except Exception as ERRO_EXCECAO:
    print(f"ERRO DE EXCEÇÃO: {ERRO_EXCECAO}")
