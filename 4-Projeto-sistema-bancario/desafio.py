# Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato

# primeira versão: implementar DEPÓSITO, SAQUE E EXTRATO.

  #DEPÓSITO: trabalhar apenas com 1 usuário, não precisa identificar qual é, E nem número da agência, e conta.
  # todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

  #SAQUE: só deve permitir realizar 3 saques diários com limite 500,00. Caso não tenha saldo em conta
  # o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo.
  # todos os saques devem ser armazenados em uma variável e exibidos na operação extrato

  # EXTRATO: deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual
  
# segunda versão: 

  # Estabelecer um limite de 10 transações diárias para conta
  # Se o usuario tentar fazer uma transação após o limite, deve ser informado que ele excedeu o número de transações permitidas
  # para quele dia
  # Mostre no extrato, a data e hora de todas as transações.
  
from datetime import datetime

menu = f"""

Olá, usuário!

Seja bem-vindo ao PyBank. Escolha uma opção do menu abaixo.

{'=' * 56}
                          MENU
{'=' * 56}

[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair

{'=' * 54}

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
  contador_de_transacoes = 1
  opcoes_menu = {0, 1, 2, 3}
  

  while True:
    try:
      data_hora = datetime.now()
      opcao = int(input(menu))
      
      if opcao not in opcoes_menu:
        print("Opção Incorreta! Digite um número constante no MENU")
      
      if opcao == 2:
        print("======================= EXTRATO ========================")
        print(f"{'Tipo':<44} {'Valor':>8}")
        print("========================================================")
        
        for lancamento in transacao:
          if lancamento["Operacao"] == "Saque":
            tipo_saque = f"{lancamento['Data']} | {lancamento['Hora']} | {lancamento['Operacao']:<21}"
            valor_saque = f"R$ ({float(lancamento['Valor']):>8.2f})"
            print(f"{tipo_saque} {valor_saque}")

          else:
            tipo_deposito = f"{lancamento['Data']} | {lancamento['Hora']} | {lancamento['Operacao']:<21}"
            valor_deposito = f"R$ {float(lancamento['Valor']):>9.2f}"
            print(f"{tipo_deposito} {valor_deposito}")

        print(f"{'=' * 56}")
        print(f"{'SALDO:':<45} {saldo:9.2f}")
        
      if opcao == 3:
          print("Obrigado por utilizar nossos serviços! Até Breve!!")
          break  
        
      if contador_de_transacoes <= 10:
        if opcao == 0: #Depositar
          deposito = float(input("Digite o valor do depósito: "))
          print(f"Depósito de R$ {deposito:.2f} efetuado com sucesso!")
          transacao.append({"Data": f"{data_hora.strftime('%d/%m/%Y')}", "Hora": f"{data_hora.strftime('%H:%M')}", "Operacao": "Deposito", "Valor": f"{deposito:.2f}"})
          atualizacao = atualizar_saldo(transacao)
          saldo = 0
          saldo = atualizacao
          contador_de_transacoes += 1
          print(f"Seu saldo é de R$: {saldo:.2f}")

        if opcao == 1: #Sacar
          if numero_saques >= LIMITE_SAQUES:
            print("Seu limite diário de 3 saques já foi atingido!")
          else:
            saque = float(input("Digite o valor do saque: "))
            if saque > saldo:
              print("Não foi possível realizar a operação. Saldo indisponível!")
            elif saque > limite:
              print("O Valor limite de saque é de R$ 500,00.")
            else:
              print(f"Saque de R$ {saque:.2f} efetuado com sucesso!")
              transacao.append({"Data": f"{data_hora.strftime('%d/%m/%Y')}", "Hora": f"{data_hora.strftime('%H:%M')}", "Operacao": "Saque", "Valor": f"{saque:.2f}"})
              atualizacao = atualizar_saldo(transacao)
              saldo = 0
              saldo = atualizacao
              print(f"Seu saldo é de R$: {saldo:.2f}")
              contador_de_transacoes += 1
              numero_saques += 1
              
      else:
        print("Você excedeu o número de transações permitidas para este dia.")
        
    except ValueError:
      print("Digite um número valido!")

sistema_bancario()
