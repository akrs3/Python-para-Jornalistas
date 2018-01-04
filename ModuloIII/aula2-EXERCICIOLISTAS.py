nomes = ['Joyce', 'Lua', 'Monnyque', 'Lua', 'Bruna', 'Monnyque']
sem_repeticao = []

for nome in nomes:
    if not nome in sem_repeticao:
        sem_repeticao.append(nome)
        
sem_repeticao.sort()
for nome in sem_repeticao:
    print(nome)

######################
sem_repeticao = set() #SET() ja pega sem repeticao

for nome in nomes:
    sem_repeticao.add(nome)
    
for nome in sorted(sem_repeticao): #um set nao tem a funcao sort(), mas tem a sorted()
    print(nome)

#########################
sem_repeticao = set(nomes) #ja pega sem repeticao
    
for nome in sorted(sem_repeticao): #um set nao tem a funcao sort(), mas tem a sorted()
    print(nome)


########## DICIONARIO

pessoa = {'nome': 'Anne', 'idade': 22}
for chave, valor in pessoa.items():
    print(str(chave) + ': ' + str(valor))
    
pessoa['sobrenome'] = 'Kelly'
del pessoa['idade']
for chave, valor in pessoa.items():
    print(str(chave) + ': ' + str(valor))