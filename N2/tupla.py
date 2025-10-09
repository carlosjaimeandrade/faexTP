#Em Python, tupla é uma estrutura de dados muito parecida com uma lista, mas com uma característica fundamental: ela é imutável.
#Ou seja, depois que você cria uma tupla, não pode alterar seus elementos (não é possível adicionar, remover ou modificar valores diretamente).

#criando uma lista com 3 tupla dentros
pontos = [
    (40.7128, -74.0060, 10),   # Nova York
    (34.0522, -118.2437, 30),  # Los Angeles
    (51.5074, -0.1278, 15)     # Londres
]

#percorrendo a lista e apresentando os valores dentro da tupla
for lat, lon, alt in pontos:
    print(f"Lat: {lat}, Lon: {lon}, Alt: {alt}m")

