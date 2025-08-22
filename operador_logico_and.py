idade = int(input("Digite sua idade: "))
nacionalidade = input("Digite sua nacionalidade: ").lower()

# Para que o bloco do if seja executado QUANDO UTILIZADO AND:
# A primeira condição precisa ser verdadeira.
# A segunda condição também precisa ser verdadeira.
# Se qualquer uma delas for falsa, o Python não entra no bloco.
if idade >= 16 and nacionalidade == "brasileiro": 
    print("Você pode votar!")
else:
    print("Você não pode votar.")
