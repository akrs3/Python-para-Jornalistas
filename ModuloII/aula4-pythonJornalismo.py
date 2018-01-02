import csv
import collections

arquivo = open('brasil.csv', encoding='utf8') #abrindo arquido leitura
populacao = collections.Counter() #cria contador vazio

#contafem a partir do CSV
for registro in csv.DictReader(arquivo):
    populacao[registro['estado']] += int(registro['habitantes']) # a = a + b / a+= b

#exibicao da contagem
#for estado, habitantes in populacao.most_common(10):
#    print('O estado ' + str(estado) + ' possui ' + str(habitantes) + ' habitantes.')

#criando arquivo de saida
arquivo_saida = open('estados.csv', mode='w', encoding='utf8')
escritor = csv.writer(arquivo, lineterminator = '\n')
escritor.writerow(['estado', 'habitantes'])
for estado, habitantes in populacao.most_common():
    escritor.writerow([estado, habitantes])

arquivo_saida.close()
    