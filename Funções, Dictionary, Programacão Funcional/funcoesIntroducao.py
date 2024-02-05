'''
Funções são trechos de código usados para repetir determinada ação 
quando chamada, por padrao retornam None
'''
def soma(a,b):
    return a + b

def cumprimento(nome):
    return f'Olá! {nome}, Boa tarde.'

print(soma(2,2))
print(cumprimento('Alexandre'))