try:
  b = float(input("Digite o valor da Base (b) em cm: "))
  h = float(input("Digite o valor da Altura (h) em cm: "))

  if b <= 0 or h <= 0:
      print("Valor inválido! Os valores digitados devem ser maior que zero.")
  else:
      Pcm = (2 * b) + (2 * h) 
      pPol = Pcm / 2.54       
      pJar = Pcm / 91.44        
      
      print(f"O valor do Perímetro em cm é de: {Pcm:.2f}")
      print(f"O valor do Perímetro em polegadas é de: {pPol:.2f}")
      print(f"O valor do Perímetro em Jardas é de: {pJar:.2f}")
except:
  print("ERRO DE EXCEÇÃO")
