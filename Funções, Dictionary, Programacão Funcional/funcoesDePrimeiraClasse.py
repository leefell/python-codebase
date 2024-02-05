''' 
é possivel passar funcoes como argumento de outras funcoes, e retornar funcoes de dentro de uma funcao
Higher Order Functions - Funções que podem receber e/ou retornar outras funções
First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)
'''

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)

v = executa(saudacao, 'Bom dia!', 'Alexandre')
print(v)