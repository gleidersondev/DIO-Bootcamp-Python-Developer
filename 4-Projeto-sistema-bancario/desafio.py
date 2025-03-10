# Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato

# primeira versão: implementar DEPÓSITO, SAQUE E EXTRATO.

  #DEPÓSITO: trabalhar apenas com 1 usuário, não precisa identificar qual é, E nem número da agência, e conta.
  # todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

  #SAQUE: só deve permitir realizar 3 saques diários com limite 500,00. Caso não tenha saldo em conta
  # o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo.
  # todos os saques devem ser armazenados em uma variável e exibidos na operação extrato

  # EXTRATO: deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual

menu = f"""

Olá, usuário!

Seja bem-vindo ao PyBank. Escolha uma opção do menu abaixo.

{'=' * 35}
               MENU
{'=' * 35}

[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair

{'=' * 35}

=> """

def atualizar_saldo (mov_transacao):
 resultado_parcial = 0
 for valores in mov_transacao:
    if(valores["Operacao"] == "Deposito"):
      resultado_parcial += float(valores["Valor"])
    else:
      resultado_parcial -= float(valores["Valor"])
 return resultado_parcial

def sistema_bancario ():
  saldo = 0
  numero_saques = 0
  limite = 500
  LIMITE_SAQUES = 3
  transacao = []

  while True:
    try:
      opcao = int(input(menu))
      
      if opcao == 0:
        deposito = float(input("Digite o valor do depósito: "))
        print(f"Depósito de R$ {deposito:.2f} efetuado com sucesso!")
        transacao.append({"Operacao": "Deposito", "Valor": f"{deposito:.2f}"})
        atualizacao = atualizar_saldo(transacao)
        saldo = 0
        saldo = atualizacao
        print(f"Seu saldo é de R$: {saldo:.2f}")

      elif opcao == 1:
        if numero_saques >= LIMITE_SAQUES:
          print("Seu limite diário de 3 saques já foi atingido!")
        else:
          saque = float(input("Digite o valor do saque: "))
          if saque > saldo:
            print("Não foi possível realizar a operação. Saldo indisponível!")
          elif saque > limite:
            print("O Valor limite de saque diário é de R$ 500,00.")
          else:
            print(f"Saque de R$ {saque:.2f} efetuado com sucesso!")
            transacao.append({"Operacao": "Saque", "Valor": f"{saque:.2f}"})
            atualizacao = atualizar_saldo(transacao)
            saldo = 0
            saldo = atualizacao
            print(f"Seu saldo é de R$: {saldo:.2f}")
            numero_saques += 1

      elif opcao == 2:
        print("============= EXTRATO =============")
        print(f"{'Tipo':<23} {'Valor':>8}")
        print("===================================")

        for lancamento in transacao:
          if lancamento["Operacao"] == "Saque":
            tipo_saque = f"{lancamento['Operacao']:<21}"
            valor_saque = f"R$ ({float(lancamento['Valor']):>8.2f})"
            print(f"{tipo_saque} {valor_saque}")

          else:
            tipo_deposito = f"{lancamento['Operacao']:<21}"
            valor_deposito = f"R$ {float(lancamento['Valor']):>9.2f}"
            print(f"{tipo_deposito} {valor_deposito}")

        print(f"{'=' * 35}")
        print(f"{'SALDO:':<24} {saldo:9.2f}")

      elif opcao == 3:
        print("Obrigado por utilizar nossos serviços! Até Breve!!")
        break

      else:
        print("Opção Incorreta! Digite um número constante no MENU")
    
    except ValueError:
      print("Digite um número valido!")

sistema_bancario()