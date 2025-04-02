class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade
    
class Funcionario(Pessoa):
  def __init__(self, nome, idade, cargo, salario):
    Pessoa.__init__(self, nome, idade)
    self.cargo = cargo
    self.salario = salario
    
class Beneficios:
  def __init__(self, vale_transporte, vale_alimentacao):
    self.vale_transporte = vale_transporte
    self.vale_alimentacao = vale_alimentacao
    
class Gerente(Funcionario, Beneficios):
  def __init__(self, nome, cargo, salario, vale_transporte, vale_alimentacao):
    Funcionario.__init__(self, cargo, salario)
    Beneficios.__init__(self, vale_transporte, vale_alimentacao)
    self.nome = nome
    
    def exibir_dados(self):