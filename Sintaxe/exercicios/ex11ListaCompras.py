import os

lista = []

while True:
    print('\n[I]nserir | [A]pagar | [L]istar')
    opc = input("Selecione uma opcao: ")

    if opc.lower().startswith('i'):
        os.system('cls')
        nome = input("Nome do produto: ")
        lista.append(nome)
    else:
        if opc.lower().startswith('a'):
            try:
                indice = input("Escolha o índice para apagar: ")
                del lista[int(indice)]
            except ValueError:
                print('Não foi possível apagar esse índice.')
            except IndexError:
                print('Indice não presente na lista.')
        else:
            if opc.lower().startswith('l'):
                os.system('cls')

                if len(lista) == 0:
                    print("Nenhum produto foi adicionado") 

                print('\nSua lista de compras: ')
                
                for item, nome in enumerate(lista):
                    print(item, '-' ,nome)
            else:
                print('Por favor, escolha I, A ou L.')
