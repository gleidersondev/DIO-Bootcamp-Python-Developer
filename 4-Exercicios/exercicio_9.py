# Que tal um programinha que junta tudo isso? Um mini caixa eletrônico que permite escolher entre
#  sacar, ver saldo e sair!

# ✅ Exibir um menu de opções
# [1] Sacar
# [2] Ver saldo
# [0] Sair

# ✅ Realizar saque
# Se o usuário escolher a opção 1 - Sacar, o programa deve:
# Pedir o valor a ser sacado.
# Verificar se há saldo suficiente.
# Se houver saldo, descontar o valor e exibir o novo saldo.
# Se não houver saldo, exibir uma mensagem de "Saldo insuficiente".

# ✅ Consultar saldo
# Se o usuário escolher a opção 2 - Ver saldo, o programa deve:
# Exibir o saldo atual da conta.

# ✅ Encerrar o programa
# Se o usuário escolher a opção 0 - Sair, o programa deve:
# Exibir uma mensagem de despedida e encerrar o loop.

# ✅ Evitar erros com entradas inválidas
# Se o usuário digitar uma opção inválida,
# o programa deve exibir uma mensagem de erro e pedir novamente a entrada.

opcoes = 0
saldo = 1500.00
saque = 0
opcao_saque = 0

while True:
  try:
    opcoes = int(input("Por favor, selecione uma das opções: \n[1] Sacar \n[2] Ver Saldo \n[0] Sair \n"))
    if opcoes == 1:
      saque = float(input("Insira o valor do saque: "))
      if saque <= saldo:
        opcao_saque = int(input(f"Deseja sacar realmente o valor de: R$ {saque:.2f}? \n[1] Sim \n[2] Cancelar \n"))
        if opcao_saque == 1:
          saldo -= saque
          print(f"Saque efetuado com sucesso! Seu saldo atual é de: R$ {saldo:.2f}")
        else:
          print("Operação cancelada")
      else:
        print("Saldo insuficiente!")
    elif opcoes == 2:
      print(f"O saldo da sua conta é de: R$ {saldo:.2f}")
    else:
      print("Obrigado por utilizar os nossos serviços! Até a próxima!!!")
      break
  except ValueError:
    print("ERRO! Digite um número válido.")

