# Desenvolva um programa que pergunte ao usuário o dia da semana (número de 1 a 7) e exiba o nome do dia correspondente.

from ast import match_case


dia_da_semana = int(input('Informe o dia da semana de 1 a 7 \n'))

match dia_da_semana:
    case 1:
        print('domingo')
    case 2:
        print('segunda')
    case 3:
        print('terça')
    case 4:
        print('quarta')
    case 5: 
        print('quinta')
    case 6:
        print('sexta')
    case 7:
        print('sabado')