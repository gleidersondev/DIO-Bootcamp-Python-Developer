# Crie um programa que permita ao usuário inserir nomes em uma lista e depois:

    # Remova um nome específico.
    # Ordene a lista em ordem alfabética.
    # Inverta a ordem da lista.

lista_nomes = []

menu = f"""

{'=' * 35}
               MENU
{'=' * 35}

Digite a opção desejada:

[1] Inserir Nome

[2] Remover Nome

[3] Ordenar em Ordem alfabética

[4] Inverter Lista

[0] Sair

{'=' * 35}


==> """


def inserir_nome():

 while True:
  try:
    msg = int(input(menu))

    if msg == 1:
      nome = str(input("Digite um nome para Incluir: "))
      lista_nomes.append(nome)
      print(f"O nome {nome} foi incluído com sucesso!")
      print(lista_nomes)

    elif msg == 2:
      if len(lista_nomes) > 0:
        remove_nome = str(input("Digite um nome para remover: " ))
        if lista_nomes.count(remove_nome) >= 1:
          lista_nomes.remove(remove_nome)
          print(f"O nome {remove_nome} foi excluído com sucesso!")
          print(lista_nomes)
        else:
          print("Esse nome não existe!")
      else:
        print("A lista está vazia!")

    elif msg == 3:
      if len(lista_nomes) > 0:
        lista_nomes.sort()
        print(lista_nomes)
      else:
        print("A Lista está vazia!")

    elif msg == 4:
      if len(lista_nomes) > 0:
        lista_nomes.sort(reverse=True)
        print(lista_nomes)
      else:
        print("A Lista está vazia!")

    elif msg == 0:
      print("Sistema Encerrado!")
      break

    else:
      print("ATENÇÃO! Digite um número contante no Menu.")

  except ValueError:
    print("Digite um número válido!!!")

inserir_nome()

   
