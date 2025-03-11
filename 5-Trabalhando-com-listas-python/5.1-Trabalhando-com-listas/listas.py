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

# Compressão

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Modificar valores

numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)