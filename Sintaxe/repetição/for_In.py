# senha = '123456'
# tentativa = ''
# repeticoes = 0

# while senha != tentativa:
#     tentativa = input(f'Sua senha ({repeticoes}x): ')

#     repeticoes += 1

# print(f'Quantidade de tentativas: {repeticoes}')
# print("O laço while é usado quando não se sabe precisamente a quantidade de repetições.")

texto = 'Agora usando o FOR'

string = ''

for letra in texto:
    string += f'*{letra}'
    print(letra)
print(string + '*')
