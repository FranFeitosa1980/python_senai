# Faça um programa que pergunte ao usuário a idade e verifique se ele pode votar (idade maior ou igual a 16).

idade = int(input('Qual sua idade? \n'))

if idade >= 16:
    print('Você pode votar')

else:
    print('Voce não pode votar')