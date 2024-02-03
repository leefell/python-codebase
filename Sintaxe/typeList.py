# """
# Listas em Python
# Tipo list - Mutável
# Suporta vários valores de qualquer tipo
# também possui índices e fatiamento
# Métodos: append, insert, pop, del, clear, extend, +
# Create Read Update  Delete
# Criar  Ler  alterar apagar = lista[i]
# """
# #        +01234
# #        -54321
# string = 'ABCDE'  # 5 caracteres (len)
# # print(bool([]))  # falsy
# # print(lista, type(lista))

# #        0    1      2              3    4
# #       -5   -4     -3             -2   -1
# lista = [123, True, 'Alexandre',  1.2, [3223]]
# lista[-3] = 'Maria'
# print(lista)
# print(lista[2], type(lista[2]))
#        0   1  2  3  4  5
lista = [10,20,30,40,50,60]
#del lista[2] # quando um elemento é deletado, todos os indices são ajustados
print(lista)

lista.append(50)
lista.append(60)
lista.append(70)
print(lista)

lista.pop()
lista.pop()
print(lista)

lista.pop(1)
print(lista)