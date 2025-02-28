try:
  tempo = int(input("Digite o tempo de permanência em segundos:"))
  horas = tempo // 3600
  minutos = (tempo % 3600) // 60
  segundos = tempo % 60
  print(f"O tempo de permanência foi de: {horas:} horas {minutos} minutos e {segundos} segundos")
except:
  print(ERRO: ERRO DE EXCEÇÃO)
