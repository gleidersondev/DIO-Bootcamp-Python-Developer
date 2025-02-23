# Crie um programa que pede a idade e verifica se a pessoa pode votar
#  (idade >= 16) e se já é obrigada a votar (idade >= 18).

idade = int(input("Digite a sua idade: "))

if idade >= 16 and idade < 18:
  print("Você já pode votar!")
elif idade >= 18:
  print("Você é obrigado a votar!")
else:
  print("Você ainda não pode votar!")
