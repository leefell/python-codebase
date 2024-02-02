# condicao = True

# while condicao:
#     nome = input("Digite seu nome: ")
#     print(f"Seu nome é {nome}")

#     break

# print('fim')

# contador = 0

# while contador < 10:
#     print(contador)
#     contador += 1

# print('fim')

'''
Operadores:
= += -= *= /= //= **= %=
'''

# continue

# contador = 0

# while contador <= 100:
#     contador += 1

#     if contador == 6:
#         print('Sem 6')
#         continue

#     if contador >= 10 and contador <= 27:
#         print("Sem mostrar o", contador)
#         continue

#     print(contador)


# while interno

qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1

print('fim')