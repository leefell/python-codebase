'''
Exiba os indices da lista
0 Alexandre
1 Gabriel
2 Marcelo
'''

lista = ['Alexandre', 'Gabriel', 'Marcelo']
lista.append('Callegari')

i = 0


for nome in lista:
    print(i, nome)
    i+=1

# outra maneira:
    
# lista = ['Alexandre', 'Gabriel', 'Marcelo']
# lista.append('Callegari')

# indices = range(len(lista))

# for indice in indices:
#     print(indice, lista[indice])
    
# outra maneira:
    
# lista = ['Maria', 'Alexandre', 'Luiz']
# lista.append('Marcelo')

# lista_enumerada = enumerate(lista)

# for nome in lista_enumerada:
#     print(nome)