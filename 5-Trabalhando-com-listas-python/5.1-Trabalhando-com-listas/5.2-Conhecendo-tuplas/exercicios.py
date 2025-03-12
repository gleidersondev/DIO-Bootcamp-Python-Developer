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


