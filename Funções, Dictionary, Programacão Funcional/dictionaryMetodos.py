# Métodos úteis de dict
# len - quantas chaves existem
# keys - iterável com as chaves
# values - iterável com as chaves
# items - iterável com as chaves e valores
# setdefault - adiciona valor se a chave ñ existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado, a ultima chave do dicionario
# update - Atualiza um dicionário com outro

# pessoa = {
#     'nome': 'Alexandre',
#     'sobrenome': 'Augusto',
#     'idade': 19
# }

# pessoa.setdefault('idade', None)
# print(pessoa['idade'])
# # print(pessoa.__len__())
# print(len(pessoa))
# print(tuple(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))

# for valor in pessoa.values():
#     print(valor)

# for chave, valor in pessoa.items():
#     print(chave, valor)

# ------------------------------------------

p1 = {
    'nome': 'Alexandre',
    'sobrenome': 'Augusto'
}

# print(p1.get('nome', 'Não existe.'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)

# ultima_chave = p1.popitem() 
# print(ultima_chave)
# print(p1)

# Update, 3 maneiras

# p1.update({
#     'nome': 'novo valor',
#     'idade' : 30,
# }) 

# p1.update(nome='novo valor', idade = 19)

tupla =(('nome', 'novo valor'), ('idade', 22)) # da pra fazer o mesmo com lista
p1.update(tupla)

print(p1)