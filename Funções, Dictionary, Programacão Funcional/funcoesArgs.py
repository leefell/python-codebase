# *args - Argumentos não nomeados
# * - *args(empacotamento e desempacotamento)
# *args é uma convenção de argumentos não nomeados

x, y, *resto = 1,2,3,4
print(x,y, resto)

# def soma(x, y):
#     return x + y

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

print(soma(1,2,3,4,5,6,432,432,231,3,4,5,6,7,32,423,4234))

numeros = 1,2,3,4,5,6,7,8,9,10
outraSoma = soma(*numeros) #desempacotando os numeros e espalhando na funcao soma
print(outraSoma)