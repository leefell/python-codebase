'''
Lista de listas e seus indices
'''

salas = [
         
    #    0           1
    ['Alexandre', 'Gabriel'], # 0    
    #   0
    ['Callegari'], # 1
    #   0         1          2          3
    ['Marcelo', 'Josue', 'Fernanda', (0,10,20,30,40)] # 2
]

# print(salas)
# print(salas[0][0])
# print(salas[0][1])
# print(salas[1][0])
# print(salas[2][0])
# print(salas[2][1])
# print(salas[2][2])
# print(salas[2][3][3]) # dessa maneira voce acessa um valor especifico dentro de uma tupla

for sala in salas:
    print(f'A sala é {sala}')
    for item in sala:
        print("Nomes: ", item)
