def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

resultado = multiplica(1,2,3,4,5)
print(resultado)

def parOuImpar(x):
    if x % 2 == 0:
        return f'{x} é Par'
    return f'{x} é Ímpar'
    
print(parOuImpar(2))
print(parOuImpar(3))
print(parOuImpar(4))
print(parOuImpar(5))