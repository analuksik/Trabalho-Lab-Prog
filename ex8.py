try:
  temp = float(input("Digite a temperatura: "))
  escala = str(input("Você digitou a temperatura em Celcius (c) ou Fahrenheit (f)? "))
  if escala == 'c':
    tempF = ((temp * 9) / 5) + 32
    print(f"A temperatura {temp}°C é {tempF:.2f}°F ")
  elif escala == 'f':
    tempC = (temp - 32) / 1.8 
    print(f"A temperatura {temp}°F é {tempC:.2f}°C ")
  else:
    print("Digite 'c' para Celsius e 'f' para Fahrenheit")
except:
  print("ERRO: ERRO DE EXECEÇÃO")
