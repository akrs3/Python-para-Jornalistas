titulo = 'Deputado Paulo Maluf se entrega à PF em São Paulo para ser preso'

url = 'https://www1.folha.uol.com.br/poder/2017/12/1944768-maluf-acerta-com-pf-e-vai-se-entregar.shtml'

'Paulo Maluf' in titulo

deputado = 'Paulo Maluf'
deputado_dos_sonhos = 'Anne Kelly'
titulo.replace(deputado,deputado_dos_sonhos)

type(titulo)

titulo.capitalize()

manchete = input('Copie e cole uma manchete qeue mencione "presidente" aqui')
manchete_modificada = manchete.lower()
novo_presidente = 'Lidiane Monteiro'
print(manchete_modificada.replace('presidente',novo_presidente))