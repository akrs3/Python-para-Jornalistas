#Como e no facebook

ID_do_aplicativo = '195401734345824'
chave_secreta = '3dac0a478ec081db56610f72c7517fbf'
token = ID_do_aplicativo + '|' + chave_secreta
pagina = 'nytimes'
url = 'https://graph.facebook.com/v2.11/' + str(pagina) + '?access_token=' + str(token)
print(url)

#No Twitter

import tweepy

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

anne = api.get_user('nytimes')._json

anne['followers_count']

jornais_no_twitter = ['folha','estadao','jornalglobo','zerohora']

def seguidores(usuario_no_twitter):
    consulta_api = api.get_user(usuario_no_twitter)._json
    seguidores = consulta_api['followers_count']
    return seguidores

seguidores['anne']

for jornal in jornais_no_twitter:
    numero = seguidores(jornal)
    frase = 'O usuario ' + jornal + ' tem ' + numero + ' seguidores no Twitter.'
    print(frase)