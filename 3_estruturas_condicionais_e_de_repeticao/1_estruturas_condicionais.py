MAIOR_IDADE = 18
IDADE_ESPECIAL = 15

idade = int(input("Qual a sua idade: "))

if idade >= MAIOR_IDADE:
  print("É maior de idade, pode tirar a CNH")

else:
  print("Ainda não pode tirar a CNH")


if idade >= MAIOR_IDADE:
  print("É maior de idade, pode tirar a CNH")
  
elif idade >= 15 and idade < MAIOR_IDADE:
  print("Pode estudar legislação")

else:
  print("Ainda não pode tirar a CNH")