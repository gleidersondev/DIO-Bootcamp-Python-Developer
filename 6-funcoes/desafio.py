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
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3

def atualizar_saldo (mov_transacao):
 resultado_parcial = 0
 print(f"O resultado parcial em alualizar saldo é {resultado_parcial}")
 for valores in mov_transacao:
    if(valores["Operacao"] == "Deposito"):
      resultado_parcial += float(valores["Valor"])
    else:
      resultado_parcial -= float(valores["Valor"])
 return resultado_parcial

def sistema_bancario (mov_transacao):
  saldo_inicial = 1000
  saldo = 0

  while True:
    try:
      opcao = int(input(menu))
      
      if opcao == 0:
        deposito = float(input("Digite o valor do depósito: "))
        print(f"Depósito de R$ {deposito:.2f} efetuado com sucesso!")
        transacao.append({"Operacao": "Deposito", "Valor": f"{deposito:.2f}"})
        print(f"O conteudo de transação é {transacao}")
        atualizacao = atualizar_saldo(mov_transacao)
        print(f" O somatorio de transação é {atualizacao}")
        saldo = 0
        print(f"O saldo é {saldo}")
        saldo = saldo_inicial + atualizacao
        mensagem = f"Seu saldo é de {saldo}"
        print(mensagem)

      elif opcao == 1:
        saque = float(input("Digite o valor do saque: "))

        print(f"Depósito de R$ {saque:.2f} efetuado com sucesso!")
        transacao.append({"Saque": f"{saque:.2f}"})
        print(transacao)
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
