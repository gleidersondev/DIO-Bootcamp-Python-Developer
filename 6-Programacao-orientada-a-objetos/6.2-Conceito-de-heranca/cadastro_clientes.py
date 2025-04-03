class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade
    
class Funcionario(Pessoa):
  def __init__(self, nome, idade, cargo, salario):
    super().__init__(self, nome, idade)
    self.cargo = cargo
    self.salario = salario
    
class Beneficios:
  def __init__(self):
    self.vale_transporte = 500
    self.vale_alimentacao = 1000
    
class Gerente(Funcionario, Beneficios):
  def __init__(self, nome, idade, salario):
    Funcionario.__init__(self, nome, idade, "Gerente", salario)
    Beneficios.__init__(self)
    self.bonus = self.salario * 0.10
  
    
    def exibir_dados(self):
      print(f"""
      
      Nome do funcionário: {self.nome}
      Idade: {self.idade}
      Cargo: {self.cargo}
      Salário: R$ {self.salario:.2f}
      Bônus: R$ {self.bonus:.2f}
      Vale Transporte: R$ {self.vale_transporte:.2f}
      Vale Alimentação: R$ {self.vale_alimentacao:.2f}
      
            """)
      