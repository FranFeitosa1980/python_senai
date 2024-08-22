# Faça um programa que peça ao usuário três números e verifique se todos são positivos

numero1 =  int(input('Informe o primeiro numero: \n'))
numero2 =  int(input('Informe o segundo numero: \n'))
numero3 =  int(input('Informe o tereiro numero: \n'))

if (numero1 >=0 and numero2 >=0 and numero3 >=0):
    print('Os numeros são positivos')

else: 
    print('Os numeros não são positivos')