'''
Operadores in e not in
String são iteráveis
 0 1 2 3 4 5 6 7 8
 A l e x a n d r e
'''
nome = 'Alexandre'
# print(nome[3]) #letra no indice 3
print('x' in nome)
print('z' in nome)
print(10 * '-')
print('x' not in nome)
print('z' not in nome)

frase = input("Digite uma frase: ")
target = input("Digite oque voce deseja saber se esta presente na frase: ")

if target in frase:
    print(f'{target} esta presente em {frase}')
else:
    print(f'{target} não esta presente em {frase}')