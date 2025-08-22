# O operador lógico not em Python é usado para inversão (negação) de valores booleanos.

# Ele transforma True em False

# E transforma False em True

lista = ['laranja', "morango", "leite"]

# if 'arroz' in lista:
#     print('ja esta na lista')
# else:
#     print('nao esta na lista')

if 'arroz' not in lista:
    print('Arroz não esta na lista')


#---------------------
# com not conseguimos tambem verificar se uma lista, string, ou dicionario esta vazio

lista = []
texto = ""
dicionarios = []

if not lista:
    print("A lista está vazia")

if not texto:
    print("A string está vazia")

if not dicionarios:
    print("O dicionário está vazio")

