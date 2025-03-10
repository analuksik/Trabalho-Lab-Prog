try:
  ingresso = float(input("Digite o valor do ingresso (R$): "))
  if ingresso <= 0:
    print("O ingresso não pode custar 0R$")
  else:
    criancas = int(input("Quantas crianças (0 a 10 anos) tinham no jogo?"))
  jovens = int(input("Quantos jovens (11 a 17 anos) tinham no jogo?"))
  adultosInt = int(input("Quantos adultos (+18 anos) foram ao jogo e não levaram meio kg de alimento?"))
  adultosMeia = int(input("Quantos adultos (+18 anos) foram ao jogo e levaram 1kg de alimento?"))
  pubTotal = criancas + jovens + adultosInt + adultosMeia
  print(f"O público total no jogo foi de: {pubTotal} pessoas")
  vJovem = (ingresso / 2) * jovens
  vAdult_int = ingresso * adultosInt
  vAdult_meia = (ingresso / 2) * adultosMeia
  valorTotal = vJovem + vAdult_int + vAdult_meia
  print(f"O valor total de arrecadação do jogo foi de: R${valorTotal:.2f}")
except:
  print("ERRO: ERRO DE EXCEÇÃO")
