"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40, 50, 60]
lista.append('Alexandre')
print(lista)
lista.pop() # vai remover o Alexandre

lista.append(1234)
print(lista)

lista.insert(5, 'Inserindo no indice 5')
print(lista)

# lista.insert(500000000, 777)
# print(lista)
# print(lista[8])

# Para deletar o último item da lista pode usar o del lista[-1]

lista.insert(0, 'Insert no indice 0')
print(lista)

print('------------------------------------------------------------------------------')

a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)

a.extend(b) # extend nao retorna nada, ele vai modificar a lista A
print(a)