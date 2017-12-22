#Expressoes boolenas e condicionais

valor = float(input('Digite um numero: '))
valor2 = float(input('Digite outro numero'))

if valor > 9000 and valor2 >9000: # Expressao booleana
    print('OVER 9K')
    print('Muito bom!')
else: # nao esta indentada
    print('Valor muito baixo =/') # esta indentada
    print('Tente novamente!')



#Calcular media e n permitir numeros negativos

valor3 = float(input('Digite um numero: '))
valor4 = float(input('Digite outro numero'))


if valor3 > 0 or valor4 >0: 
    media = (valor3 +valor4)/2
    print('A média é:' + str(media))
else: 
    print('Valor negativos! =/') 
    print('Tente novamente!')