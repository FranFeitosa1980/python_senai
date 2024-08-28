# Crie um programa que peça ao usuário 10 números e exiba apenas os números pares.

numeros = []

for i in range(10):
    numero = int(input('Informe um numero: \n'))
    numeros.append(numero)

for numero in numeros:
    if numero %2 ==0:
        print(numero,' ',end='')
    
print('São pares')
