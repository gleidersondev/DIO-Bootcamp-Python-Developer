# Peça para o usuário digitar um e-mail e verifique:

    # Se ele contém "@gmail.com" ou "@hotmail.com"
    # Extraia apenas o nome de usuário (parte antes do "@")
    # Exiba um menu formatado usando strings triplas

# msg = f"""


# ============= MENU =============
# Usuário detectado: {nome_usuario}
# Seu provedor de e-mail é aceito.  
# ================================


# """
# print(nome_usuario)
# print(provedor)

while True:
  try:
    email_usuario = input("Digite seu email: ").lower().strip().replace(" ", "")

    index_referencia = email_usuario.index("@")
    nome_usuario = email_usuario[:index_referencia]
    provedor = email_usuario[index_referencia:]

    msg = f"""


        ============= MENU =============
        Usuário detectado: {nome_usuario}
        Seu provedor de e-mail é aceito.  
        ================================


        """

    if provedor == "@gmail.com" or provedor == "@hotmail.com":
      print(msg)
      break
    else:
      print("PROVEDOR DE EMAIL NÃO ACEITO. Utilize '@gmail.com' ou '@hotmail.com'")
  except ValueError:
    print("UTILIZE UM EMAIL VÁLIDO.")

