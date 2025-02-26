# Peça para o usuário digitar um e-mail e verifique:

    # Se ele contém "@gmail.com" ou "@hotmail.com"
    # Extraia apenas o nome de usuário (parte antes do "@")
    # Exiba um menu formatado usando strings triplas

email_usuario = input("Digite seu email: ").lower().strip().replace(" ", "")
print(email_usuario)

index_referencia = email_usuario.index("@")
nome_usuario = email_usuario[:index_referencia]
provedor = email_usuario[index_referencia:]
print(nome_usuario)
print(provedor)

while True:
  try:
    if provedor == "@gmail.com" or provedor == "@hotmail.com":
      
