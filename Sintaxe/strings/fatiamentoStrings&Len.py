"""
Fatiamento de strings
 012345678
 Olá mundo
 Fatiamento [inicio:fim:passo] [::]
 Função len retorna a qtd de caracteres da string
"""
variavel =  'Olá mundo'
print(variavel[4:]) #aqui vai imprimir a string a partir do indice 4
print(variavel[0:])

#len
#indices vao de 0 - 8
# a contagem conta os caracteres, 1,2,3,4,5,6,7,8
print(len(variavel))

print(variavel[0:8:2])
               #[inicio:fim:passo]
print(variavel[::-1]) #inverte a string
