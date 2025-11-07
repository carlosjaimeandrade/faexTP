# A palavra-chave def é usada para definir uma função em Python.
# Uma função serve para organizar o código em blocos reutilizáveis, 
# ou seja, você escreve um trecho uma vez e pode chamá-lo sempre que precisar.
#exemplo1
def nome_da_funcao(parametros):
    # bloco de código
    return parametros

#exemplo 2
def saudacao():
    print("Olá! Seja bem-vindo ao sistema.")

#como chamar a função
saudacao()

#exemplo 3
def somar(a, b):
    resultado = a + b
    return resultado
#como chamar a função
soma = somar(1,3)
soma2 = somar(1,3)
print(soma)
print(soma2)

#Exemplo junto com try e entrada de dados
def ler_numero():
    while True:
        try:
            num = float(input("Digite um número: "))
            return num
        except ValueError:
            print("Valor inválido! Tente novamente.")

n1 = ler_numero()
n2 = ler_numero()
print("A soma é:", n1 + n2)