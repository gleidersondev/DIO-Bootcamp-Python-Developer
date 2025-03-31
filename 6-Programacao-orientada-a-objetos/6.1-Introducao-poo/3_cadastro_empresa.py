class Empresa:
  def __init__(self, nome, cnpj, faturamento):
    self.nome = nome
    self.cnpj = cnpj
    self.faturamento = faturamento
    
  def calcular_imposto(self):
    bc = (float(self.faturamento) * 0.32)
    irpj_normal = bc * 0.15
    irpj = ((irpj_normal - 20000) * 0.10) + irpj_normal if irpj_normal > 20000 else bc 
    csll = bc * 0.09
    return irpj, csll
  
  def exibir_dados(self):
    irpj, csll = self.calcular_imposto()
    print(f"""
    A empresa {self.nome}, inscrita no CNPJ nº {self.cnpj}, apresentou o seguinte faturamento no período:
    
    R$ {float(self.faturamento):.2f}.
    
    O imposto devido foi:
    IRPJ R$ {irpj:.2f}
    CSLL R$ {csll:.2f}
    
    """)
    

  
  
      
    
    
    
    