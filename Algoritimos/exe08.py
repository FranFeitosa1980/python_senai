# Desenvolva um algoritmo que pergunte ao usuário o estado civil (solteiro, casado, divorciado, viúvo) e exiba uma mensagem correspondente.

estado_civil = str(input('Informe seu estado civil: solteiro, casado, divorciado, viúvo \n'))

match estado_civil:
    case 'solteiro':
        print('Você é solteiro!')
    case'casado':
        print ('Você é casado!')
    case 'divorciado':
        print('Você é divorciado!')
    case'viuvo': 
        print('Você é viúvo!')