# 1️⃣ Controle de Usuários Cadastrados

# 📌 Situação: Você tem um sistema e deseja verificar se um novo usuário já está cadastrado.

# 🔹 Desafio:

#        Crie um conjunto de usuários cadastrados e um novo conjunto com usuários que tentaram se registrar.

#        Exiba quais usuários já estão cadastrados e quais são novos


usuarios_cadastrados = {"alice", "bob", "carla", "daniel"}
novos_usuarios = {"bob", "daniel", "eva", "fernando"}

# Verificar quais já estão cadastrados
print(f"Já estão cadastrados: {usuarios_cadastrados.intersection(novos_usuarios)}")
print(f"São novos usuários: {novos_usuarios.difference(usuarios_cadastrados)}")


# 2️⃣ Filtrando Produtos Repetidos no Carrinho

# 📌 Situação: Em um e-commerce, um usuário adiciona produtos ao carrinho, mas pode ter itens repetidos.

# 🔹 Desafio:
#         Crie uma lista com produtos e remova os duplicados usando um conjunto.


carrinho = ["notebook", "mouse", "teclado", "mouse", "monitor", "teclado"]

carrinho_unico = set(carrinho)

print("Produtos no carrinho (sem repetição):", carrinho_unico)



# 3️⃣ Detectando Palavras Proibidas em Comentários

# 📌 Situação: Você quer bloquear comentários que contenham palavras proibidas.

# 🔹 Desafio:

#     Defina um conjunto de palavras proibidas.
#     Peça ao usuário para digitar um comentário e verifique se ele contém alguma palavra proibida.

palavras_proibidas = {"ofensa", "palavrão", "xingamento"}







# 4️⃣ Comparando Estoques de Duas Lojas

# 📌 Situação: Você tem duas lojas e quer saber quais produtos estão disponíveis em ambas e quais são exclusivos de cada loja.

# 🔹 Desafio:

#     Crie conjuntos com os produtos de cada loja.
#     Exiba quais produtos estão nas duas lojas e quais são exclusivos de cada uma.

loja1 = {"celular", "tablet", "notebook", "mouse"}
loja2 = {"notebook", "mouse", "impressora", "monitor"}