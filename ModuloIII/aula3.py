#FUNCOES E BIBLIOTECAS PYTHON
#link da documentacao das bibliotecas:    https://docs.python.org/3/library/

def hello(nome):
    #nome = input('Digite aqui seu nome:')
    print('Olá ' + nome)

hello('Kelly')
print(len('Anne'))
hello()

seu_nome = input ('Digite seu nome:')
hello(seu_nome)

def primeiro_nome(nome_completo):
    nome_completo = nome_completo.strip().title()
    primeiro = nome_completo.split(' ')[0]
    return primeiro

#print(primeiro_nome(nome))

nome = input('Digite seu nome:')

def genero(nome_completo):
    if primeiro_nome(nome_completo).endswith('o'):
        return 'masculino'
    elif primeiro_nome(nome_completo).endswith('a'):
        return 'feminino'
    else:
        return 'nao sei'
    
print(genero('Anna Kelly'))
print(genero('Paulo'))

nomes = ['Anna Kelly', 'Paulo Vinicius', 'Ailton Junior', 'Monnyque Bulhoes']
for nome in nomes:
    print(nome + ' é do genero ' + genero(nome))