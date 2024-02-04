'''
Iterando strings com while
'''    #012345678
nome = 'Alexandre'
indice = 0
novoNome = ''

while indice < len(nome):
    letra = nome[indice]
    novoNome += f'*{letra}'
    indice += 1

novoNome += '*'    
print(novoNome)