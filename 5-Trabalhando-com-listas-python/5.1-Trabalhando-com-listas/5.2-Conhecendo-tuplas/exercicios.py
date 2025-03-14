# Dada a seguinte tupla com nomes de carros:
  
carros = ("Gol", "Uno", "Celta", "Palio", "Fiesta", "Sandero", "Civic", "Corolla", "Hilux", "Fusca")

# 1️⃣ Acesse elementos da tupla usando fatiamento:

#     Exiba os três primeiros carros.
#     Exiba os três últimos carros.
#     Exiba a tupla na ordem inversa.

# 2️⃣ Utilize um método de tupla para contar quantas vezes o carro "Gol" aparece na tupla.

# 3️⃣ Utilize um método de tupla para descobrir em qual posição está o carro "Civic".

# 4️⃣ Itere sobre a tupla e exiba os nomes dos carros que possuem mais de 5 letras.
  
  
# 1
tres_primeiros = carros[0:3]
print(tres_primeiros)

tres_ultimos = carros[-3:]
print(tres_ultimos)

inverso = carros[::-1]
print(inverso)

# 2

contador = carros.count("Gol")
print(contador)

# 3

posicao = carros.index("Civic")
print(posicao)

# 4

def verifica_carros():
  carros_com_mais_de_cinco_letras = []
  for index in carros:
    if len(index) > 5:
      carros_com_mais_de_cinco_letras.append(index)
  if len(carros_com_mais_de_cinco_letras) == 0:
    print("Não existe nenhum carro com mais de 5 letras na lista")
  else:
    print(carros_com_mais_de_cinco_letras)
    
verifica_carros()    


