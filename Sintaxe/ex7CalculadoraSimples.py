print('Calculadora simples de dois números')

condicao = True

while condicao:
    n1 = input("\nDigite o primeiro número: ")
    n2 = input("Digite o segundo número: ")

    inteiroN1 = float(n1)
    inteiroN2 = float(n2)

    opcao = input("Escolha a operação: \n+ - Somar \n- - Subtrair \n / Dividir \n * Multiplicar \nSua escolha: ")

    if opcao == '+':
        operacao = inteiroN1 + inteiroN2
    elif opcao == '-':
        operacao = inteiroN1 - inteiroN2
    elif opcao == '/':
        operacao = inteiroN1 / inteiroN2
    elif opcao == '*':
        operacao = inteiroN1 * inteiroN2
    else:
        print("Opção Invalida.")
        break

    print(f"O resultado da operação é: {operacao}")
    continuar = input("Deseja Sair? [S]im [N]ao: ")

    if continuar.lower().startswith('s'):
        condicao = False