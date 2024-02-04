# underline é uma convenção de uma variavel que existe mas não seria usada pra nada

# nome1, *resto = ['Maria', 'Helena', 'Alexandre']
# print(nome1, resto)

# _, _, nome, *resto = ['Maria', 'Helena', 'Alexandre']
# print(nome, resto)

# Desempacotamento em chamadas de métodos e funções
string = 'ABCD'
lista = ['Maria', 'Alexandre', 1,2,3,4, 'Helena']
tupla = 'Eu', 'Sou', 'o', 'Batman.'

# primeiro, b, *resto, ultimo = lista
# print(primeiro, ultimo)

print(*string) # 'tudo de'
print(*lista)
print(*tupla)