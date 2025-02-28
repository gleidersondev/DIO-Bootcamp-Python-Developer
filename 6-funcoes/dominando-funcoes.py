# Primeira função
def exibir_mensagem():
    print("Olá mundo!")

exibir_mensagem()

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

exibir_mensagem_2(nome="Gleiderson")

# Retorno de valores

def calcular_total(numeros):
    return sum(numeros)


def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

print(calcular_total([1,2,3]))
print(retorna_antecessor_e_sucessor(10))

# Argumentos Nomeados
def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})