frase = 'a pior coisa que eu posso ser é igual a todo mundo, eu odeio isso.'

i = 0
qtdMaisVezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    atual = frase[i]

    if atual == ' ':
        i += 1
        continue

    qtd_atual = frase.count(atual)

    if qtdMaisVezes < qtd_atual:
        qtdMaisVezes = qtd_atual
        letra_apareceu_mais_vezes = atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtdMaisVezes}x'
)
