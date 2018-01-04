#criar lista de nomes
#criar lista de dicionarios, para cada nome da 1 lista, cria um dicionario
#o dicionario tem nome e genero

nomes = ['Anne','Sabrina', 'Amanda','Alana']
lista_dicionarios = []
for nome in nomes:
    dicionario = {'nome':nome, 'genero':'feminino'}
    lista_dicionarios.append(dicionario)
    
print(lista_dicionarios)