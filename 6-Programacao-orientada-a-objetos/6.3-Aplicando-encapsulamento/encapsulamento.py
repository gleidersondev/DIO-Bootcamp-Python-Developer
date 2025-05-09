# class Conta:
#     def __init__(self, nro_agencia, saldo=0):
#         self._saldo = saldo
#         self.nro_agencia = nro_agencia

#     def depositar(self, valor):
#         # ...
#         self._saldo += valor

#     def sacar(self, valor):
#         # ...
#         self._saldo -= valor

#     def mostrar_saldo(self):
#         # ...
#         return self._saldo


# conta = Conta("0001", 100)
# conta.depositar(100)
# print(conta.nro_agencia)
# print(conta.mostrar_saldo())

class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def idade(self):
        _ano_atual = 2022
        return _ano_atual - self._ano_nascimento


pessoa = Pessoa("Guilherme", 1994)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")
