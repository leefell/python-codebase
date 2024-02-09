"""
Closure e funcoes que retornam outras funcoes
Closure é uma função que "lembra" o ambiente em que foi criada. Isso significa 
que a função pode acessar e operar com variáveis que não estão localmente definidas dentro dela 
mas que estavam no escopo da função que a envolveu quando foi definida.
"""
def saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

bomDia = saudacao('Bom dia')
boaNoite = saudacao('Boa noite')

#print(saudacao1()) # esse parenteses é o closure, onde ele obriga o compilador a lembrar 

for nome in ['Maria', 'Joana', 'Alexandre']:
    print(bomDia(nome))
    print(boaNoite(nome))