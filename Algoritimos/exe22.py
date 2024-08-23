# Escreva um programa que peça ao usuário para inserir dois números e verifique se o primeiro é maior que o segundo.

numero_1 = int(input('Digite o primeiro numero: \n'))
numero_2 = int(input('Digite o segundo numero: \n'))

if numero_1 >= numero_2:
    print('O primeiro numero é maior que o segundo')
else:
    print('O segundo número é maior que o primeiro')