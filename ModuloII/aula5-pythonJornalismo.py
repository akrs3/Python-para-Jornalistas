ID_do_aplicativo = '195401734345824'
chave_secreta = '3dac0a478ec081db56610f72c7517fbf'
token = ID_do_aplicativo + '|' + chave_secreta
pagina = 'nytimes'
url = 'https://graph.facebook.com/v2.11/' + str(pagina) + '?access_token=' + str(token)
print(url)

knight = {
   "name": "Knight Center for Journalism in the Americas",
   "id": "48853626794"
}

knight['name']
#retorna "Knight Center for Journalism in the Americas"