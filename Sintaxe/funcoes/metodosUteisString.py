'''
split e join com list e string
split = divide a string
join = une a string
'''
string = "Eu gosto muito da Franquia: Batman Arkham."
listaPalavras = string.split()
listaFrases = string.split(':') 
print(listaPalavras)

listaFrases2 = []
# strip tira espacos do comeco e do fim, existe o rstrip e lstrip (right, left)
for i, frase in enumerate(listaFrases):
    listaFrases2.append(listaFrases[i].strip()) 

# print(listaFrases)
# print(listaFrases2)

uniaoFrases = ','.join(listaFrases)
print(uniaoFrases)