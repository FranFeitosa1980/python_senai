# Crie um programa que solicite ao usuário dois números e exiba a soma, subtração, multiplicação e divisão entre eles.


numero_1 = int(input('Digite o primeiro numero \n' ))
numero_2 = int(input('Digite o segundo numero \n'))

operacao = str(input('Escolha uma operação matematica: + , - , * , / \n'))

match operacao:
    case '+' :
        print('o resultado é :' , numero_1 + numero_2)
    
    case '-' :
        print('o resultado é :' , numero_1 - numero_2)
    
    case '*' :
        print('o resultado é :' , numero_1 * numero_2)
    
    case '/' :
        print('o resultado é :' , numero_1 / numero_2)
    