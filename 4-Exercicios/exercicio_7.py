# Peça um número ao usuário e exiba a tabuada desse número de 1 a 10.

numero = int(input("Digite um número: "))
for i in range(11):
  print(i * numero, end=",")