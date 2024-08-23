# Crie um programa que solicite ao usuário três números e exiba o maior deles.

numero_1 = int(input('Digite o primeiro numero: \n'))
numero_2 = int(input('Digite o segundo numero: \n'))
numero_3 = int(input('Digite o tereiro numero: \n'))

if (numero_1 > numero_2 and numero_1 > numero_3 ):
    print('O maior número é o primeiro : ')
elif (numero_2 > numero_1 and numero_2 > numero_3 ):
    print('O maior número é o segundo : ')
else:
    print('O maior número é o terceiro: ')