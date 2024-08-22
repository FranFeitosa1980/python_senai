# Escreva um algoritmo que peça ao usuário para digitar um número e verifique se ele é maior, menor ou igual a 10.

numero = int(input('Digite um numero: \n'))

if numero == 10:
    print('Numero igual a 10')
elif numero <= 10:
    print('Numero menor que 10')
else: 
    print('Numero maior que 10')