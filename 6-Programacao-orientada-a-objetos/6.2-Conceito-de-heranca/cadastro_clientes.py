class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade
    
class Funcionario(Pessoa):
  def __init__(self, nome, idade, cargo, salario):
    Pessoa.__init__(self, nome, idade)
    self.cargo = cargo
    self.salario = salario