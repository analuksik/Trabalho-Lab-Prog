try:
  av1 = float(input("Digite sua nota da AV1: "))
  av2 = float(input("Digite sua nota da AV2: "))
  faltas = int(input("Quantas faltas você teve? "))
  horas = float(input("Qual a carga horária da matéria? "))
  pMinima = horas * 0.25
  media = (av1 + av2) / 2
  if faltas > pMinima:
    print("Reprovado por faltas! ")
  elif media >= 7:
    print("Aprovado!")
  elif media < 3:
    print("Reprovado por nota! ")
  elif (media) < 7:
    print("Prova Final! ")
    pf = float(input("Qual foi a sua nota na prova final? "))
    if pf > 5:
      print("Aprovado na Prova Final! ")
    else:
      print("Reprovado!")
except Exception as ERRO_EXCECAO:
  print(f"ERRO DE EXCEÇÃO: {ERRO_EXCECAO}")
  
