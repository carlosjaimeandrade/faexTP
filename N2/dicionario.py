# Um dicionário simples de um "usuário"
usuario = {
    "nome": "Ana Silva",
    "idade": 28,
    "email": "ana.silva@exemplo.com",
    "ativa": True
}

print(usuario)
#pegando por chave
print(usuario['nome'])
#adicionanod uma nova chave e valor
usuario['possui_credito'] = False

#podemos ter um array de dicionario
usuarios = [
    {
        "nome": "Ana Silva",
        "idade": 28,
        "email": "ana.silva@exemplo.com",
        "ativa": True
    },
    {
        "nome": "Carlos",
        "idade": 38,
        "email": "carlos.jaime@exemplo.com",
        "ativa": False
    }
]

#cada valor dentro é um index ou seja 
#se eu quero o pegar o primeiro index (dicionario 0) 
print(usuarios[0])
#caso queira printar apenas o nome do primeiro index
print(usuarios[0]['nome'])

#posso utilizar o for para poder pecorrer todos os indices
#index representa cada index do array, só é possivel por causa do enumerate utilizando ele o 
#python retona o index para cada valor, junto com a lista de fato que vamos percorrer
#exemplo 
#[
#    (0, {'nome': 'Ana Silva', 'idade': 28}),
#    (1, {'nome': 'Carlos', 'idade': 38})
#]
for index, usuario in enumerate(usuarios):
    print(usuario['nome'])
    #adicionando novo dado a todo momento que percorre
    usuario['id'] = index

print(usuarios)