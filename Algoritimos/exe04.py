# Crie um algoritmo que solicite ao usuário uma cor (vermelho, verde, azul) e exiba uma mensagem correspondente à cor escolhida.

cor = input('Informe uma cor entre vermelho, verde, azul \n')

match cor:
    case 'vermelho':
        print('vermelhou o curral')
    case'verde':
        print ('esverdeou como o Huck')
    case 'azul':
        print('azul como o mar')