# Faça um programa que solicite ao usuário dois números e verifique se ambos são pares.

numero_1 = int(input('Informe o primeiro numero \n'))
numero_2 = int(input('Informe o segundo numero \n'))

if (numero_1 % 2 == 0 and numero_2 % 2 == 0):
     print('Os numeros são pares')

else:
    print('Os numeros não são pares')
