class Empresa:
  def __init__(self, nome, cnpj, faturamento):
    self.nome = nome
    self.cnpj = cnpj
    self.faturamento = faturamento
    
  def calcular_imposto(self):
    bc = (float(self.faturamento) * 0.32) * 0.15
    irpj = ((bc - 20000) * 0.10) + bc if bc > 20000 else bc
  
  
      
    
    
    
    