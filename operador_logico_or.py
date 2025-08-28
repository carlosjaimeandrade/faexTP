# Pede ao usuário para digitar um nome de usuário
usuario = input("Digite seu usuário: ")

# Verifica se o valor digitado é "admin" OU "professor"
# O operador "or" significa: basta UMA das duas condições ser verdadeira
if usuario == "admin" or usuario == "professor":
    # Se o usuário digitou "admin" ou "professor", cai aqui
    print("Acesso liberado!")
else:
    # Se não digitou nenhum dos dois, cai aqui
    print("Acesso negado!")
