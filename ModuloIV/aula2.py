#https://dadosabertos.camara.leg.br/api/v2/deputados   -- html da api dos deputadoes
#https://dadosabertos.camara.leg.br/api/v2/deputados?formato=json

import requests
import csv

deputados = []
url = 'https://dadosabertos.camara.leg.br/api/v2/deputados'
url_deputado = ''
arquivo_saida = open('deputados.csv', encoding='utf8',mode='w')
escritor = csv.writer(arquivo_saida,lineterminator = '\n')
escritor.writerow(['nome','uri','uriPartido','sigla Partido','sigla UF', 'id Legislatura','url Foto',])

for pagina in [1,2,3,4,5,6]:
    print(pagina)
    parametros = {'formato': 'json', 'itens': 100, 'pagina': pagina}
    resposta = requests.get(url,parametros)
    #print(resposta.text) #obter o html da pagina como string
    #print(resposta.json()) #obter o html da pagina como json, converte json em dicionario

    for deputado in resposta.json()['dados']:
        #print(str(deputado['nome']) + ' (' + str(deputado['siglaPartido']) + ')')
        #print(f'{deputado['nome']} ({deputado['siglaPartido']})') ERRO
        escritor.writerow([deputado['nome'], deputado['uri'] , deputado['uriPartido'],deputado['siglaPartido'] ,deputado['siglaUf'] ,deputado['idLegislatura'] ,deputado['urlFoto']])
        deputados.append(deputado['nome'])

print(len(deputados))
arquivo_saida.close()