#  Escreva um programa que pergunte ao usuário uma idade e verifique se a pessoa é adolescente (entre 13 e 17 anos).

idade = int(input('Informe uma idade: \n'))

if (idade>=13) and (idade<=17):
    print('Você é adolescente')
else:
    print('Você não é adolescente')