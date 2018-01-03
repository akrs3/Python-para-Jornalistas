import csv
import collections

arquivo = open('brasil.csv', encoding='utf8') #abrindo arquido leitura
populacao = collections.Counter() #cria contador vazio
area = collections.Counter() # criar contador vazio para area
densidade = collections.Counter()

#contafem a partir do CSV
#for registro in csv.DictReader(arquivo):
#    populacao[registro['estado']] += int(registro['habitantes'])

#contafem a partir do CSV
for registro in csv.DictReader(arquivo):
    area[registro['estado']] += float(registro['area'])
    populacao[registro['estado']] += int(registro['habitantes'])
    densidade[registro['estado']] = populacao[registro['estado']] / area[registro['estado']]

#exibicao da contagem
#for estado, habitantes in populacao.most_common(10):
#    print('O estado ' + str(estado) + ' possui ' + str(habitantes) + ' habitantes.')

#criando arquivo de saida
arquivo_saida = open('densidade.csv', mode='w', encoding='utf8')
escritor = csv.writer(arquivo_saida, lineterminator = '\n')
escritor.writerow(['Estado', 'Habitantes', 'Área', 'Densidade'])
for registro['estado'], densidade in densidade.most_common():
    escritor.writerow([registro['estado'], populacao[registro['estado']], area[registro['estado']], densidade])

arquivo_saida.close()
    