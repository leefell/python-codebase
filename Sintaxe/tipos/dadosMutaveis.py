"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)

lista é um iteravel, e o for funciona com ela
"""
listaA = ['Alexandre', 'Maria', 1, True, 1.2]
listaB = listaA.copy()

listaA[1] = 'Fernanda'
print(listaB)
print(listaA)

for item in listaA:
    print(item)

# semelhante ao foreach do c#