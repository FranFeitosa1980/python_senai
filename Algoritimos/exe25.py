# Escreva um programa que peça ao usuário um número de 0 a 20 e verifique se ele está entre 10 e 15.

numero = int(input('Digite um numero de 0 a 20: \n'))

if numero >= 10 and numero <=15:
    print('O numero digitado está entre 10 e 15')

else: 
    print('O numero digitado não está entre 10 e 15')