# Crie um programa que solicite ao usuário um número de 1 a 12 e exiba o mês correspondente.

numero = int(input('Digite um número de 1 a 12: \n'))

match numero:
    case 1:
        print('Janeiro')
    case 2:
        print('Fevereiro')
    case 3:
        print('Março')
    case 4:
        print('Abril')
    case 5:
        print('Maio')
    case 6:
        print('Junho')
    case 7:
        print('Julho')
    case 8:
        print('Agosto')
    case 9:
        print('Setembro')
    case 10:
        print('Outubro')
    case 11:
        print('Novembro')
    case 12:
        print('Dezembro')