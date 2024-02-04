'''
For + range
range -> range(start,stop,step)
'''
# numeros = range(1,10,1)

# for numero in numeros:
#     print(numero)

for i in range(10):
    if i == 2:
        print('i é 2, proximo...')
        continue

    if i == 8:
        print('i é 8')
        break

    for j in range(1,3):
        print(i,j)
else:
    print('completo com sucesso.')