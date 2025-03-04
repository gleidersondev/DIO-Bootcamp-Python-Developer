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

transacao = []

def atualizar_saldo (mov_transacao):
 resultado_parcial = 0
 print(f"O resultado parcial em alualizar saldo é {resultado_parcial}")
 for valores in mov_transacao:
    if(valores["Operacao"] == "Deposito"):
      resultado_parcial += float(valores["Valor"])
    else:
      resultado_parcial -= float(valores["Valor"])
 print(f"resultado dentro de atualiza saldo {resultado_parcial}")
 return resultado_parcial

def sistema_bancario (mov_transacao):
  saldo = 0
  numero_saques = 0
  limite = 500
  LIMITE_SAQUES = 3
  mensagem = f"Seu saldo é de {saldo}"

  while True:
    try:
      opcao = int(input(menu))
      
      if opcao == 0:
        deposito = float(input("Digite o valor do depósito: "))
        print(f"Depósito de R$ {deposito:.2f} efetuado com sucesso!")
        transacao.append({"Operacao": "Deposito", "Valor": f"{deposito:.2f}"})
        atualizacao = atualizar_saldo(mov_transacao)
        saldo = 0
        saldo = atualizacao
        print(f"o saldo é de: {saldo:.2f}")
        print(mensagem)

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
            transacao.append({"Operacao": "Saque", "Valor": f"{saque:.2f}"})
            atualizacao = atualizar_saldo(mov_transacao)
            print(f"O valor do saque é {atualizacao}")
            saldo = 0
            saldo = atualizacao
            print(f"O saldo final é {saldo}")
            print(mensagem)
            numero_saques += 1
            print(f"Numero de saques {numero_saques}")

      elif opcao == 2:
        print("Extrato")



    
    except ValueError:
      print("Digite um número valido!")

sistema_bancario(transacao)


# ========== EXTRATO ==========
# Tipo                 Valor     
# ==============================
# Depósito             R$ 100.00
# Saque                R$ 50.00
# Depósito             R$ 200.00

# Saldo final: R$ 250.00
# ============================
