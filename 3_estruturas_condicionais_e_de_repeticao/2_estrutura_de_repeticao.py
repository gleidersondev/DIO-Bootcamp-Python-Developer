texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

print(texto)

for indice in texto:
  if indice.upper() in VOGAIS:
    print(indice, end=" ")

print()