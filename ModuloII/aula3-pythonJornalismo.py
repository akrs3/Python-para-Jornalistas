import csv

populacao = 0
estado_desejado = input('Digite a sigla: ')
estado_desejado = estado_desejado.upper()

arquivo = open('brasil.csv', encoding='utf8')

for registro in csv.DictReader(arquivo):
    if registro['estado'] == estado_desejado:
        populacao += int(registro['habitantes']) # a = a + b / a+= b

print(populacao)