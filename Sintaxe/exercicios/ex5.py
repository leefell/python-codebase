"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

entrada = input("Digite um número inteiro: ")

if entrada.isdigit():
    n = int(entrada)
    if(n % 2 == 0):
        print("O número é par.")
    else:
        print("O número é impar.")
else:
    print("O número não é inteiro.")


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horario = input("Digite a hora em números inteiros: ")

horarioInt = int(horario)

if(horarioInt >= 0 and horarioInt <= 11):
    print("Bom dia!")
elif(horarioInt >= 12 and horarioInt <= 17):
    print("Boa tarde!")
else:
    print("Boa noite!")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
 
"""

nome = input("Digite seu primeiro nome: ")
tamanho = len(nome)

if tamanho > 1:
    if tamanho <= 4:
        print("Seu nome é curto")
    elif tamanho >= 5 and tamanho <= 6:
        print("Seu nome é normal")
    else:
        print("Seu nome é muito grande")
else:
    print("Digite mais de uma letra")
