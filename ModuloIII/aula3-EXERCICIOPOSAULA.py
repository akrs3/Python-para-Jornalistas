import csv

#Importa arquivo csv base
arquivo = open('politicos_outubro.csv',encoding='utf-8')
sem_repeticao = []

#define as funcoes primeiro nome e genero
def primeiro_nome(nome_completo):
    nome_completo = nome_completo.strip().title()
    primeiro = nome_completo.split(' ')[0]
    return primeiro

def genero(nome_completo):
    prim_nome = primeiro_nome(nome_completo)
    if prim_nome.endswith('o') | prim_nome.endswith('s') | prim_nome.endswith('m'):
        return 'masculino'
    elif prim_nome.endswith('a') | prim_nome.endswith('si'):
        return 'feminino'
    else:
        return 'nao sei'


#Guardar nomes dos politicos, sem repeticao
for registro in csv.DictReader(arquivo):
    if not registro['nome'] in sem_repeticao:
        sem_repeticao.append(str(registro['nome']))

#Criar arquivo de saida e colocar o nome dos campos
arquivo_saida = open('politicos_genero',mode='w',encoding='utf-8')
escritor = csv.writer(arquivo_saida, lineterminator= '\n')
escritor.writerow(['Nome','Genero'])


#Preencher o arquvio de saida com Nomes e Generos
for nome in sorted(sem_repeticao):
    gen = genero(nome)
    escritor.writerow([nome,gen])

arquivo_saida.close()