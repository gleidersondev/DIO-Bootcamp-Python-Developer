# Estrutura Condicional e Identação
# MAIOR_IDADE = 18
# IDADE_ESPECIAL = 15

# idade = int(input("Qual a sua idade: "))

# if idade >= MAIOR_IDADE:
#   print("É maior de idade, pode tirar a CNH")

# else:
#   print("Ainda não pode tirar a CNH")

# if idade >= MAIOR_IDADE:
#   print("É maior de idade, pode tirar a CNH")
  
# elif idade >= 15 and idade < MAIOR_IDADE:
#   print("Pode estudar legislação")

# else:
#   print("Ainda não pode tirar a CNH")


saldo = 2000
saque = 3000
cheque_especial = 450

conta_normal = False
conta_universitaria = True

if conta_normal:
  if saque <= saldo:
    print("Saque realizado com sucesso")
  elif saque <= (saldo + cheque_especial):
    print("Saque realizado usando limite do cheque especial")
  else:
    print('Não foi possível realizar o saque, saldo insuficiente!')
elif conta_universitaria:
  if saque <= saldo:
    print("Saque em conta universitaria realizado com sucesso")
  elif saque <= (saldo + cheque_especial):
    print("Saque realizado em conta universitaria usando limite do cheque especial")
  else:
    print('Não foi possível realizar o saque em conta universitaria, saldo insuficiente!')
else:
  print("Não foi possível reconhecer seu tipo de conta, entre em contato com seu gerente")