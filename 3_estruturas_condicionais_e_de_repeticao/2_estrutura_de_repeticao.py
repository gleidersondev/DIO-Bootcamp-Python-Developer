# FOR

# texto = input("Informe um texto: ")
# VOGAIS = "AEIOU"

# print(texto)

# for indice in texto:
#   if indice.upper() in VOGAIS:
#     print(indice, end=" ")

# print()

# FOR / ELSE

# numeros = [1, 3, 5, 7, 9]

# for num in numeros:
#     if num == 3:
#         print("Número encontrado!")
#         break  # Interrompe o loop se encontrar
# else:
#     print("Número não encontrado.")  # Executa se o break NÃO for acionado

# FOR com RANGE
# tabuada do cinco
# for i in range(0, 51, 5):
#   print(i, end=",")

# while

opcao = -1

while opcao != 0:
    try:
        opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))
        
        if opcao == 1:
            print("Sacando....")
        elif opcao == 2:
            print("Exibindo extrato....")
        elif opcao == 0:
            print("Saindo...")
        else:
            print("Opção inválida! Tente novamente.")

    except ValueError:
        print("Erro! Digite um número válido.")

