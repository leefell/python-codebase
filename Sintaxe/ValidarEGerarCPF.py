# Validador de cpfs

import re # expressoes regulares
import sys

entrada = input("CPF: ")

cpf_enviado_usuario = re.sub(
    r'[^0-9]', 
    '', 
    entrada
    #alternativa: cpf_enviado_usuario = '746.824.890-70'.replace('.', '').replace('-', '')
)

entradaSequencial = entrada == entrada[0] * len(entrada)

if entradaSequencial:
    print('Você enviou dados sequencias.')
    sys.exit()

noveDigitos = cpf_enviado_usuario[:9]
contadorRegressivo1 = 10

resultadoDigito1 = 0

for digito1 in noveDigitos:
    resultadoDigito1 += (int(digito1) * contadorRegressivo1)
    contadorRegressivo1 -= 1
digito1 = (resultadoDigito1 * 10) % 11
digito1 = digito1 if digito1 <= 9 else 0
print('O primeiro digito do cpf é: ', digito1)

dezDigitos = noveDigitos + str(digito1)
contadorRegressivo2 = 11
resultadoDigito2 = 0

for digito2 in dezDigitos:
    resultadoDigito2 += (int(digito2) * contadorRegressivo2)
    contadorRegressivo2 -= 1
digito2 = (resultadoDigito2 * 10) % 11
digito2 = digito2 if digito2 <= 9 else 0
print('O segundo digito do cpf é: ', digito2)

cpf_gerado_pelo_calculo = f'{noveDigitos}{digito1}{digito2}'

if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf_enviado_usuario} é válido')
else:
    print('CPF inválido')

# Gerador de cpfs.
# Para criar um gerador de cpfs validos, comente o código de cima e descomente o debaixo

# import random
# for _ in range(100):
#     noveDigitos = ''
#     for i in range(9):
#         noveDigitos += str(random.randint(0,9))
        
#     # Calcula o primeiro dígito verificador do CPF
#     contadorRegressivo1 = 10
#     resultadoDigito1 = 0
#     for digito1 in noveDigitos:
#         resultadoDigito1 += (int(digito1) * contadorRegressivo1)
#         contadorRegressivo1 -= 1
#     digito1 = (resultadoDigito1 * 10) % 11
#     digito1 = digito1 if digito1 <= 9 else 0

#     # Concatena os nove dígitos do CPF com o primeiro dígito verificador
#     cpf_sem_verificador = f'{noveDigitos}{digito1}'

#     # Calcula o segundo dígito verificador do CPF
#     contadorRegressivo2 = 11
#     resultadoDigito2 = 0
#     for digito2 in cpf_sem_verificador:
#         resultadoDigito2 += (int(digito2) * contadorRegressivo2)
    #     contadorRegressivo2 -= 1
    # digito2 = (resultadoDigito2 * 10) % 11
    # digito2 = digito2 if digito2 <= 9 else 0

    # # Concatena o segundo dígito verificador ao CPF
    # cpf_gerado = f'{cpf_sem_verificador}{digito2}'

    # # Exibe o CPF gerado
    # print(f'CPF gerado: {cpf_gerado}')