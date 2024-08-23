# Escreva um programa que peça ao usuário para inserir três números e verifique se todos são iguais.

numero_1 = int(input('Digite o primeiro numero: \n'))
numero_2 = int(input('Digite o segundo numero: \n'))
numero_3 = int(input('Digite o tereiro numero: \n'))

if (numero_1 == numero_2 and numero_1 == numero_3 and numero_2 == numero_3):
    print('Os número são iguais')
else:
    print('Os números são diferentes')
