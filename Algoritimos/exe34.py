# Escreva um programa que peça ao usuário um número e verifique se ele é positivo, negativo ou zero.

numero = int(input('Digite um numero: \n'))

if numero >0:
    print('Numero é positivo')

elif numero <0:
    print('Numero é negativo')

else:
    print('Numero igual a 0')