preco = float(input("Digite o preço da mercadoria: "))
reaj = str(input("Você deseja o valor com acréscimo ou com desconto? "))
if reaj == 'acrescimo':
  precoFinal = preco * 1.03
elif reaj == 'desconto':
  precoFinal = preco * 0.97
print(f"O valor da mercadoria é de: R${precoFinal:.2f} ")
