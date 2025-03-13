try:
  a = float(input("Digite o valor de a: "))
  b = float(input("Digite o valor de b: "))
  c = float(input("Digite o valor de c: "))
  if a < 0 or b < 0 or c < 0:
    print("O valor deve ser positivo!")
  elif a < (b + c)  and b < (a + c) and c < (a + b):
    print("É um triângulo!")

    if a == b == c:
      print("É um Triângulo Equilátero")
    elif a == b or a == c or b == c:
      print("É um Triângulo Isósceles")
    else: 
      print("É um triângulo Escaleno")
  else: 
    print("Não é um Triângulo")
except Exception as ERRO_EXECAO:
  print(f"ERRO DE EXCEÇÃO: {ERRO_EXECAO}")
