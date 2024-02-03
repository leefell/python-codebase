import os

palavraSecreta = 'achocolatado'
acertos = ''
n_tentativas = 0

condicao = True

while condicao:
    tentativa = input("Digite uma letra: ")
    n_tentativas += 1
    
    if len(tentativa) > 1:
        print("Digite apenas uma letra.")
        continue

    if tentativa in palavraSecreta:
        acertos += tentativa

    palavraFormada = ''

    for tentativa in palavraSecreta:
        if tentativa in acertos:
            palavraFormada += tentativa
        else:
            palavraFormada += '*'

    print('Palavra formada: ', palavraFormada)

    if palavraFormada == palavraSecreta:
        os.system('cls')
        print("Voce acertou, parabens!")
        print('A palavra era,', palavraSecreta)
        print('Tentativas:', n_tentativas)
        acertos = ''
        n_tentativas = 0