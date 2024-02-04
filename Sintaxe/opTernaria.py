# Condicional de uma linha
condicao = 10 == 11
variavel = 'Valor' if condicao else 'Outro valor'
print(variavel)

digito = 1
# novoDigito = digito if digito <= 9 else 0 
novoDigito = 0 if digito > 9 else digito 
print(novoDigito)

# possivel mas nao recomendado
# print('Valor' if False else 'Outro valor' if False else 'Fim')