Learn Python - (www.codeacademy.com/pt)
Datacamp (www.datacemp.com)
Udemy (udemy.com)
EdX(www.edx.org)

#Painel das bolhas do Meio com PSEU_CÓDIGO

#Usa uma definicao de perfis de direita e esquerda
#Pega os links que esses perfis compartilham
#Rankea os links em popularidade
#Entrega os resultados

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

perfis_politicos = {'esquerda': ['jeanwyllys_real'], 'direita': ['jairbolsonaro']}

api.user_timeline('jairbolsonaro')

def pega_links(perfil):
    #Entrar na API
    #usar user_timeline do perfil
    #Pegar a lista de resultados e achar o que e url
    #return [lista de links]