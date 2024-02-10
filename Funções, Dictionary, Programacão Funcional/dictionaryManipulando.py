pessoa = {}  # Criar um dicionário vazio.

chave = 'nome'  # Definir uma chave dinâmica.

pessoa[chave] = 'Alexandre'  # Adicionar uma entrada com a chave 'nome' e o valor 'Alexandre'.
pessoa['sobrenome'] = 'Augusto'  # Adicionar uma entrada com a chave 'sobrenome' e o valor 'Augusto'.

print(pessoa[chave])  # Imprimir o valor associado à chave dinâmica.

pessoa[chave] = 'Gabriel'  # Atualizar o valor associado à chave dinâmica.

del pessoa['sobrenome']  # Deletar a entrada associada à chave 'sobrenome'.
print(pessoa)  # Imprimir o dicionário após as modificações.
print(pessoa['nome'])  # Imprimir o valor associado à chave 'nome' após a atualização.

if pessoa.get('sobrenome') is None:
    print("Chave não existe.")
else:
    print("Sobrenome = ", pessoa['sobrenome'])