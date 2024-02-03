# underline é uma convenção de uma variavel que existe mas não seria usada pra nada

# nome1, *resto = ['Maria', 'Helena', 'Alexandre']
# print(nome1, resto)

_, _, nome, *resto = ['Maria', 'Helena', 'Alexandre']
print(nome, resto)