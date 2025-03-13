try:
  n1 = int(input("Digite o 1º número: "))
  n2 = int(input("Digite o 2º número: "))

  if n1 == n2:
    print("Erro de entrada: Os números devems ser distintos! ")

  n3 = int(input("Digite o 3º número: "))
  if n1 == n3 or n2 == n3:
    print("Erro de entrada: Os números devems ser distintos! ")

  n4 = int(input("Digite o 4º número: "))
  if n1 == n4 or n2 == n4 or n3 == n4:
    print("Erro de entrada: Os números devems ser distintos! ")

  n5 = int(input("Digite o 5º número: "))
  if n1 == n5 or n2 == n5 or n3 == n5 or n4 == n5:
    print("Erro de entrada: Os números devems ser distintos! ")

  else:
    somaPares = 0
    somaImpar = 0
    contPares = 0
    contImpar = 0

  if n1 % 2 == 0:
    somaPares += n1
    contPares += 1
  else:
    somaImpar += n1
    contImpar += 1

  if n2 % 2 == 0:
    somaPares += n2
    contPares += 1
  else:
    somaImpar += n2
    contImpar += 1

  if n3 % 2 == 0:
    somaPares += n3
    contPares += 1
  else:
    somaImpar += n3
    contImpar += 1

  if n4 % 2 == 0:
    somaPares += n4
    contPares += 1
  else:
    somaImpar += n4
    contImpar += 1

  if n5 % 2 == 0:
    somaPares += n5
    contPares += 1
  else:
    somaImpar += n5
    contImpar += 1

  mediaPares = somaPares / contPares
  mediaImpar = somaImpar / contImpar

  print(f"A média dos números Ímpares é {mediaImpar} ")
  print(f"A média dos números Pares é {mediaPares} ")
except Exception as ERRO_EXECAO:
  print(f"ERRO DE EXCEÇÃO: {ERRO_EXECAO}")
