# Desenvolva um programa que pergunte ao usuário para inserir 10 números e, ao final, exiba a média dos números inseridos.

numeros = []

for i in range(10):
    numero = float(input('Informe um numero: \n'))
    numeros.append(numero)
  
for numero in numeros:
    total = sum(numeros) / 10
    
print('A media dos números é: ', total)