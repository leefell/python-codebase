# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Fulano',
#     'sobrenome': 'Ciclano',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }

# pessoa = dict(nome='gabriel', sobrenome='tangerina') # usado mais em sobreposicoes 

pessoa = {
    'nome': 'Alexandre',
    'sobrenome': 'Augusto',
    'idade': 19,
    'altura': 1.8,
    'enderecos': [
        {'rua': 'rua 1', 'numero': 123},
        {'rua': 'rua 2', 'numero': 321}
    ],
}

#acessar
print(pessoa['nome'])
print(pessoa['enderecos'])

for chave in pessoa:
    print(chave, pessoa[chave])