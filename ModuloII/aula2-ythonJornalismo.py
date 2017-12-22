import csv

populacao = 0
estado_desejado = input('Qual o estado desejado?')
estado_desejado = estado_desejado.upper()

arquivo = open('brasil.csv', encoding='utf8')
for registro in csv.reader(arquivo):
    habitantes = registro[2]
    estado = registro[0]
    
    if estado == estado_desejado:
        populacao += int(habitantes) # a = a + b / a+= b
        #print(registro)
print(populacao)
               