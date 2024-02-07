'''
Criar funcoes que duplicam, triplicam e quadruplicam um número
'''

# def duplica(n):
#     return n * 2

# def triplica(n):
#     return n * 3

# def quadriplica(n):
#     return n * 4

def criarMultiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criarMultiplicador(2)
triplicar = criarMultiplicador(3)
quadriplicar = criarMultiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadriplicar(2))