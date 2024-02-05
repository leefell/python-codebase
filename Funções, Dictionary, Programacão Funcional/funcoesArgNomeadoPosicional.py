# Argumentos nomeados têm um nome precedido por um sinal de igual "="
# Argumentos não nomeados recebem apenas o valor do argumento

# def soma(a,b,c):
#     print(f'{a=} {b=} {c=}', '|', 'a + b + c = ', a + b + c)

# soma(1,2,3) # isso são argumentos posicionais
# soma(1, b=2, c=5) # isso são argumentos nomeados

# -----------------------------------------------------------

'''
Ao definir uma função, os parâmetros podem ter valores padrão.
Caso o valor não seja enviado como parâmetro, o compilador usa o valor padrão.
'''

def soma(a, b, c=None):
    if c is not None:
        print(f'{a=} {b=} {c=}', '|', 'a + b + c = ', a + b + c)
    else:
        print(f'{a=} {b=}', '|', 'a + b = ', a + b)

soma(1, 2)  # Chamada sem o parâmetro 'c', usará o valor padrão
soma(3, 5)  # Chamada sem o parâmetro 'c', usará o valor padrão
soma(100, 200)  # Chamada sem o parâmetro 'c', usará o valor padrão
soma(7, 9, 0)  # Chamada com todos os parâmetros especificados
