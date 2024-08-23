# Desenvolva um algoritmo que peça ao usuário para digitar dois números e verifique se a multiplicação deles é igual a 20.

numero_1 = int(input('Digite o primeiro número:\n'))
numero_2 = int(input('Digite o segundo número: \n'))

if numero_1 * numero_2 == 20:
    print('Numeros multiplicados é igual a 20')
else:
    print('Numeros multiplicados diferente de 20')