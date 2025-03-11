try:
  m = float(input("Digite o valor da massa: "))
  uMedida = str(input("A massa digitada foi em onça (oz), tonelada (t) ou quilograma (kg)? "))
  if uMedida == 'quilogramas' or uMedida == 'kg':
    print(f"{m} kg equivalem a {(m / 0.0283495):.2f} onças e {(m / 1000):.6f} toneladas ")
  elif uMedida == 'oz' or uMedida == 'onça':
    print(f"{m} oz equivalem a {(m * 0.0283495):.6f} kg e {(m * 0.0283495 / 1000):.6f} toneladas ")
  elif uMedida == 'toneladas' or uMedida == 't':
    print(f"{m} tonelada equivalem a {(m * 1000):.2f} kg e {(m * 1000 / 0.0283495):.2f} onças ")
  else:
    print("Erro: Dados de entrada inválidos")
except:
  print("ERRO: ERRO DE EXCEÇÃO") 
