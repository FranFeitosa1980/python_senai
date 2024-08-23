# Escreva um programa que peça ao usuário para inserir uma palavra e verifique se ela tem mais de 5 letras.

palavra = str(input('Escreva uma palavra\n'))


if len (palavra) >5:
    print('Esta palavra tem mais de 5 letras')

else:
    print('Esta palavra tem menos de 5 letras')
