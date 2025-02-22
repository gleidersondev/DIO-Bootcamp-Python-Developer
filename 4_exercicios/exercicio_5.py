# Peça ao usuário para digitar uma palavra e verifique se a letra "a" está presente nela.

palavra = str(input("Digite uma palavra: "))
print(palavra)

if "a" in palavra:
  print(f"A letra 'a' consta na palavra {palavra}")
else:
  print(f"A letra 'a' não consta na palavra {palavra}")
