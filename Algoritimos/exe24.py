# Desenvolva um algoritmo que pergunte ao usuário o nome de uma cidade e verifique se é a capital do Brasil.

cidade = str(input('Informe o nome de uma cidade \n'))

if cidade == 'Brasília' or cidade == 'brasília':
    print('Essa é a capital do Brasil')

else: 
    print('Esta cidade não é a capital do Brasil')