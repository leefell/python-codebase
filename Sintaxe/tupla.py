'''
Tupla = lista IMUTÁVEL
Se você precisa de uma coleção de elementos que não pretende alterar, use uma tupla.
Não são usados colchetes.
'''
nomes = 'Maria', 'Alexandre', 'Luiz'

nomes = tuple(nomes)
print(nomes)

nomes = list(nomes)
print(nomes)