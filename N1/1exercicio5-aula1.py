# 5) Solicite ao usuário o valor total da compra. Aplique um desconto progressivo conforme o valor:
# Compras até R$ 100,00: 5% de desconto
# Compras entre R$ 100,01 e R$ 500,00: 10% de desconto
# Compras acima de R$ 500,00: 15% de desconto
# Calcule e apresente:
# O valor original da compra
# O percentual de desconto aplicado
# O valor do desconto
# O valor final a pagar
# Formula para obter percentual de desconto 
# (desconto* totalCompra)/100


# Solicita ao usuário o valor total da compra
total_compra = float(input("Digite o valor total da compra: R$ "))

# Verifica qual percentual de desconto aplicar conforme as faixas de valor
if total_compra <= 100:
    percentual_desconto = 5
elif total_compra <= 500:
    percentual_desconto = 10
else:
    percentual_desconto = 15

# Calcula o valor do desconto usando a fórmula
valor_desconto = (percentual_desconto * total_compra) / 100

# Calcula o valor final da compra
valor_final = total_compra - valor_desconto

# Exibe os resultados formatados
print(f"\nValor original da compra: R$ {total_compra:.2f}")
print(f"Percentual de desconto aplicado: {percentual_desconto}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor final a pagar: R$ {valor_final:.2f}")
