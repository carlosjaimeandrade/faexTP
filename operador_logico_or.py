# Para que o bloco do if seja executado QUANDO UTILIZADO OR :

# Se a primeira condição for verdadeira, o Python não verifica a segunda, porque já sabe que o resultado será True.

# Se a primeira condição for falsa, aí sim ele verifica a segunda.

# O bloco só não será executado se todas as condições forem falsas.


email = input("Digite o token de acesso: ")
senha = input("Digite sua senha: ")

if senha != "1234" or email != "carlos.jaime@faex.edu.br":
    print("Acesso negado!")
else:
    print("Acesso permitido!")