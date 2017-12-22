#Formato de Dados: csv, 
#baixa o csv em bit.ly/brasilcsv

arquivo = open('brasil.csv', encoding='utf8')
for linha in arquivo:
    print(linha)