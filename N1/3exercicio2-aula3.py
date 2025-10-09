# Imagine que você está organizando uma festa e deseja permitir a entrada das pessoas que sejam convidadas ou que tenham comprado ingresso.

# Regras:
# O usuário deve informar se possui convite (sim ou não)
# O usuário deve informar se comprou ingresso (sim ou não)
# A entrada será permitida se a pessoa tiver convite ou ingresso.

# Solicita ao usuário se ele possui um convite
convite = input("Você possui convite? (sim ou não): ").strip().lower()
# .strip() remove espaços extras antes e depois da resposta
# .lower() transforma a resposta em letras minúsculas para facilitar a comparação

# Solicita ao usuário se ele comprou ingresso
ingresso = input("Você comprou ingresso? (sim ou não): ").strip().lower()
# Mesmo tratamento de strip() e lower() para padronizar a resposta

# Verifica se a pessoa pode entrar
# A entrada será permitida se a pessoa tiver convite ou ingresso
if convite == "sim" or ingresso == "sim":
    print("Entrada permitida! Bem-vindo à festa!")
else:
    print("Entrada negada! Você precisa de convite ou ingresso.")
