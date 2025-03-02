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

transacao = [

]

saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3

def sistema_bancario ():
  while True:
    try:
      opcao = int(input(menu))
      if opcao == 0:
        deposito = float(input("Digite o valor do depósito: "))
        print(f"Depósito de R$ {deposito:.2f} efetuado com sucesso!")
        transacao.append({"Operacao": "Deposito", "Valor": f"{deposito:.2f}"})
        for valores in transacao:
          resultado = 0
          mensagem = f"Seu saldo é de {saldo + resultado}"
          if(valores["Operacao"] == "Deposito"):
            resultado += float(valores["Valor"])
            print(mensagem)
          else:
            resultado -= float(valores["Valor"])
            print(mensagem)
        print(transacao)
      elif opcao == 1:
        saque = float(input("Digite o valor do saque: "))
        print(f"Depósito de R$ {saque:.2f} efetuado com sucesso!")
        transacao.append({"Saque": f"{saque:.2f}"})
        print(transacao)
      elif opcao == 2:
        print("Extrato")



      
    

    except ValueError:
      print("Digite um número valido!")

sistema_bancario()


# ========== EXTRATO ==========
# Tipo                 Valor     
# ==============================
# Depósito             R$ 100.00
# Saque                R$ 50.00
# Depósito             R$ 200.00

# Saldo final: R$ 250.00
# ============================
