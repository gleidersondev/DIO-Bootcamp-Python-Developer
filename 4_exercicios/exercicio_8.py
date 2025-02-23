# Crie um programa que peça uma senha ao usuário e só encerre quando a senha correta for digitada.

senha_correta = "Python123"

senha = input("Digite sua senha: ")

while senha != senha_correta:
  print("Senha Incorreta. Tente novamente!")
  senha = input("Digite sua senha: ")

print("Senha correta!")  





