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

# Append

lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)

# Clear

lista = [1, "Python", [40, 30, 20]]

print(lista) 

lista.clear()

print(lista)

# Copy

lista = [1, "Python", [40, 30, 20]]

lista.copy()

print(lista)

# Count

cores = ["vermelho", "azul", "verde", "azul"]

print(cores.count("vermelho")) 
print(cores.count("azul")) 
print(cores.count("verde"))


# Extend

linguagens = ["python", "js", "c"]

print(linguagens) 

linguagens.extend(["java", "csharp"])

print(linguagens)


# Index