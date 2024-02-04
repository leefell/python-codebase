# Caso precise de um número absurdamente preciso pode fazer desse jeito:

# import decimal as dec

# n1 = dec.Decimal('0.1')
# n2 = dec.Decimal('0.7')

n1 = 0.1
n2 = 0.7
n3 = n1 + n2
print(n3)
print(f'{n3:.2f}')
print(round(n3))
print(round(n3, 2))