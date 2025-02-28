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