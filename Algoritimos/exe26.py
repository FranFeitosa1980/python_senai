#  Desenvolva um algoritmo que peça ao usuário para inserir dois números e verifique se ambos são múltiplos de 5.

numero_1= int(input('Digite o primeiro numero: \n'))
numero_2 = int(input('Digite o segundo numero: \n'))

if numero_1 % 5 == 0 and numero_2 % 5 == 0: 
    print('Os numeros digitados são multiplos de 5')

else: 
    print('Os numeros digitados não são multiplos de 5')
