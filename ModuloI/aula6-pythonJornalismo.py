#Quiz do Buzzfeed
#1. Mostrar opcoes
#2. Capturar os inputs
#3. Calcular resultado, baseado nos inputs

#insuportabilidade = int(input('De 0 a 30, quao chato voce é:'))
insuportabilidade =0;

resposta1 = input("Voce gosta de fazer cocegas nas pessoas")
if resposta1 == 's':
    insuportabilidade = insuportabilidade +1
    
resposta2 = input("Voce imita os outros para irritar")
if resposta2 == 's':
    insuportabilidade = insuportabilidade +1

#respostas
if insuportabilidade == 0:
    print('Voce e a pessoa MAIS LEGAL DO MUNDO')
elif insuportabilidade > 0 and insuportabilidade < 10:
    print('Voce nao e perfeito!')
elif insuportabilidade > 10 and insuportabilidade < 25:
    print('Deus me livre e guarde')
else:
    print('Talvez voce seja muito chato!')