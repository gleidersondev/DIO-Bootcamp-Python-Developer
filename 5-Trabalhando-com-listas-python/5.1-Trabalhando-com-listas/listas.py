# Declarando listas

frutas = ["maçã", "laranja", "uva", "pera"]

# Acesso direto

print(frutas[2])
print(frutas[-1])

# Matriz

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0]) 
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

# Iteração

carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)


for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")