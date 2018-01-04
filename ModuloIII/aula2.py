#listas:    num = [0,1,2,3]   acesso num[0] num(-1) -> pega o ultimo
#           slices pegam fatias e devolvem essa listaimport random

#JOGO DA SALADA MISTA
#Define-se a lista de jogadores
jogadores = ['Anne', 'Raira', 'Lidy', 'Crush 1', 'Sapao', 'Anfibio']

#Mostrar em ordem alfabetica
jogadores.sort()
for jogador in jogadores:
    print(jogador)
    
selecionado = random.choice(jogadores)

print('Seleciona: ' + selecionado)

opcoes = ['pera','uva', 'maca', 'salada mista']
#opcoes2 = ('pera','uva', 'maca', 'salada mista') # TUPLA = lista imutavel
resposta = input(selecionado + ', qual opcao vc escolhe?')

if resposta in opcoes:
    #selecionar felizardo
    jogadores.remove(selecionado)
    felizardo = random.choice(jogadores)
    jogadores.append(selecionado)
    
    if resposta == 'pera':
        print(selecionado + ', de a mao a ' + felizardo)
    elif resposta == 'uva':
        print(selecionado + ', de um abraco em ' + felizardo)
    elif resposta == 'maca':
        print(selecionado + ', de um beijo no rosto de ' + felizardo)
    elif resposta == 'salada mista':
        print('Beija, beija, beija' + felizardo)
        
else:
    print(selecionado + ', voce nao sabe jogar Salada Mista?!')

