lista = [10, 20, 30, 40, 50]
print("Lista inicial:", lista, "\n")

# 1. Acessar elementos
print("1) Acessar elementos: lista[0] ->", lista[0])

# 2. Alterar elementos
lista[1] = 25
print("2) Alterar elementos: lista[1] = 25 ->", lista)

# 3. Tamanho da lista
print("3) Tamanho da lista: len(lista) ->", len(lista))

# 4. Adicionar no final
lista.append(60)
print("4) Adicionar no final: append(60) ->", lista)

# 5. Inserir em posição específica
lista.insert(2, 15)
print("5) Inserir em posição específica: insert(2, 15) ->", lista)

# 6. Estender lista com outra
lista.extend([70, 80])
print("6) Estender com outra lista: extend([70, 80]) ->", lista)

# 7. Remover elemento pelo valor
lista.remove(25)
print("7) Remover pelo valor: remove(25) ->", lista)

# 8. Remover pelo índice
retirado = lista.pop(3)
print("8) Remover pelo índice: pop(3) ->", lista, "| Removido:", retirado)

# 9. Apagar todos os elementos
temp = lista.copy()
temp.clear()
print("9) Limpar lista: clear() ->", temp)

# 10. Encontrar índice de um valor
print("10) Índice do valor 50: lista.index(50) ->", lista.index(50))

# 11. Contar ocorrências
lista2 = [1, 2, 2, 3, 2, 4]
print("11) Contar ocorrências de 2:", lista2.count(2))

# 12. Ordenar lista
lista3 = [5, 1, 4, 3, 2]
lista3.sort()
print("12) Ordenar lista crescente: sort() ->", lista3 )

# 13. Ordenar decrescente
lista3.sort(reverse=True)
print("13) Ordenar decrescente: sort(reverse=True) ->", lista3)

# 14. Retornar lista ordenada sem alterar a original
print("14) sorted(lista3):", sorted(lista3))

# 15. Inverter a lista
lista3.reverse()
print("15) Inverter ordem: reverse() ->", lista3)

# 16. Copiar lista
copia = lista3.copy()
print("16) Copiar lista: copy() ->", copia)

# 17. Fatiamento
print("17) Fatiamento: lista[1:4] ->", lista[1:4])

# 18. Concatenar listas
print("18) Concatenar listas: [1,2] + [3,4] ->", [1,2] + [3,4])

# 19. Repetir lista
print("19) Repetir lista: [1,2] * 3 ->", [1,2] * 3)
