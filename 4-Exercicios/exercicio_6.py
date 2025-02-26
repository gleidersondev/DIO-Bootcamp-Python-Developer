# Crie um programa que verifica se um número digitado pelo usuário é positivo, negativo ou zero.

numero = int(input("Digite um núero: "))

if numero == 0:
  print(f"O número digitado é {numero}")
elif numero > 0:
  print(f"O número digitado é positivo")
else:
  print("O número digitado é negativo")