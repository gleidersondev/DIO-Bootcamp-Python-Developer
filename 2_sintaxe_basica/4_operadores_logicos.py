saldo = 1000
saque = 250
limite = 200
conta_especial = True

expressao_1 = saldo <= saque
print(expressao_1)

expressao_2 = saldo >= saque and saque <= limite
print(expressao_2)

expressao_3 = saldo >= saque or saque <= limite
print(expressao_3)

expressao_4 = not conta_especial
print(expressao_4)