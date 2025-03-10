try:
  preco = float(input("Digite o preço da mercadoria: "))
  reaj = str(input("Você deseja o valor com acréscimo ou com desconto? "))
  vReaj = float(input("Qual o valor (%) de reajuste você deseja?"))
  if reaj == 'acrescimo':
    precoFinal = preco * (1 + vReaj / 100)
  elif reaj == 'desconto':
    precoFinal = preco * (1 - vReaj / 100)
  print(f"O valor da mercadoria é de: R${precoFinal:.2f} ")
except:
  print("ERRO: ERRO DE EXCEÇÃO")
