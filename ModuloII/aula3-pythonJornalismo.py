import csv

populacao = 0
densidade = 0
estado_desejado = input('Digite a sigla do estado: ')
estado_desejado = estado_desejado.upper()

arquivo = open('brasil.csv', encoding='utf8')

for registro in csv.DictReader(arquivo):
    if registro['estado'] == estado_desejado:
        densidade = int(registro['habitantes']) / float(registro['area'])
        municipio = registro["municipio"]
        #populacao += int(registro['habitantes']) # a = a + b / a+= b
        print('Densidade de ' + str(municipio) + ' eh: ' +  str(densidade))

#print('A populacao de ' + estado_desejado  + ' eh: ' + str(populacao))
#print(f'A populacao de {estado_desejado} eh: {populacao}') NAO PEGOU