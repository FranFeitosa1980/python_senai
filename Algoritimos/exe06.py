    # Desenvolva um programa que pergunte ao usuário uma operação matemática (+, -, *, /) e dois números, e realize a operação escolhida.


operacao = str(input('Escolha uma operação matematica: + , - , * , / \n'))
numero_1 = int(input('Digite o primeiro numero \n' ))
numero_2 = int(input('Digite o segundo numero \n'))

match operacao:
    case '+' :
        print('o resultado é :' , numero_1 + numero_2)
    
    case '-' :
        print('o resultado é :' , numero_1 - numero_2)
    
    case '*' :
        print('o resultado é :' , numero_1 * numero_2)
    
    case '/' :
        print('o resultado é :' , numero_1 / numero_2)
    