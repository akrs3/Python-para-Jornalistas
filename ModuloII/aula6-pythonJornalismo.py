import csv
import collections

arquivo = open('politicos_outubro.csv',encoding='utf-8')
dicionario = csv.DictReader(arquivo)

total_posts = collections.Counter()
compartilhamentos_top = 0
linha_top = ''
politico_topzera = ''

for linha in dicionario:
    #politico = linha['nome']
    #total_posts[politico] += 1
    if int(linha['shares']) > compartilhamentos_top: #num copartilhamento atual > num MAX compartilhamentos ate agroa
        compartilhamentos_top = int(linha['shares']) #link do post bombado
        link_top = linha['fb_link']
        politico_topzera = linha['nome']
        print('Novo lider do ranking eh:' + str(politico_topzera))

print('Chefe, quem bombou mesmo foi o ' + str(politico_topzera) + ', o post dele teve ' + str(compartilhamentos_top) + ' compartilhamentos. Voce pode ler o post neste link: ' + str(link_top))
total_posts.most_common()
    