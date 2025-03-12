
try:
  m = float(input("Digite o valor da massa: "))
  uMedida = input("A massa digitada foi em onça (oz), tonelada (t) ou quilograma (kg)? ")
  
  if uMedida in ('quilograma', 'kg'):
      print(f"{m} kg equivalem a {(m / 0.0283495):.2f} onças e {(m / 1000):.6f} toneladas.")
  
  elif uMedida in ('onça', 'oz'):
      print(f"{m} oz equivalem a {(m * 0.0283495):.6f} kg e {(m * 0.0283495 / 1000):.6f} toneladas.")
  
  elif uMedida in ('tonelada', 't'):
      print(f"{m} tonelada(s) equivalem a {(m * 1000):.2f} kg e {(m * 1000 / 0.0283495):.2f} onças.")
  
  else:
      print("Unidade inválida. Use 'kg', 'oz' ou 't'.")
except:
  print("ERRO: ERRO DE EXCEÇÃO")
