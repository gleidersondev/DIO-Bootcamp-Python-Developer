# Declaração

frutas = (
    "laranja",
    "pera",
    "uva",
)
print(frutas)

letras = tuple("python")
print(letras)

numeros = tuple([1, 2, 3, 4])
print(numeros)

pais = ("Brasil",)
print(pais)

# Acesso direto

frutas = ("maçã", "laranja", "uva", "pera",)

print(frutas[0])  
print(frutas[2])  


# Indices negativos
frutas = (
    "maçã",
    "laranja",
    "uva",
    "pera",
)

print(frutas[-1])  
print(frutas[-3])  

# Matriz

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

print(matriz[0])  
print(matriz[0][0])  
print(matriz[0][-1]) 
print(matriz[-1][-1]) 


# Fatiamento

tupla = ("p", "y", "t", "h", "o", "n",)

print(tupla[2:])
print(tupla[:2])
print(tupla[1:3]) 
print(tupla[0:3:2]) 
print(tupla[::]) 
print(tupla[::-1])


# Iterar

carros = (
    "gol",
    "celta",
    "palio",
)

for carro in carros:
    print(carro)


for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")


# Count

cores = (
    "vermelho",
    "azul",
    "verde",
    "azul",
)

print(cores.count("vermelho")) 
print(cores.count("azul")) 
print(cores.count("verde")) 


# Index

linguagens = ("python", "js", "c", "java", "csharp",)

print(linguagens.index("java")) 
print(linguagens.index("python")) 

# len

linguagens = (
    "python",
    "js",
    "c",
    "java",
    "csharp",
)

print(len(linguagens)) 