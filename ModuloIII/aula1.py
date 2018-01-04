#nomes = input('Insira os nomes separados por virgula:')
nomes2 = '''ANNE Kelly
Lidiane Monteiro
RAIRA Oliveira
Mateus Castro
Esdras Rodrigues
Rubson Lima
Carmen Miranda''' #String 1 tem 3 linhas 

lista_de_nomes  = nomes.split(',') #separa a string dada em varias as strings pela ,
lista_de_nomes2 = nomes2.splitlines() #separa a string dada em varias as strings pelo ENTER

for nome_completo in lista_de_nomes2:
    nome_completo = nome_completo.strip().title()
    primeiro_nome = nome_completo.split(' ')[0]
    if (primeiro_nome.endswith('o') | primeiro_nome.endswith('s')):
        print(nome_completo + ' é homem.')
    elif (primeiro_nome.endswith('a') | primeiro_nome.endswith('e')):
        print(nome_completo + ' é mulher.')
    else:
        print(nome_completo + ' nao sei.')