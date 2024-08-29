# Escreva um algoritmo que forneça um menu para o usuário: 1-Cadastrar nome, 2- atualizar o nome, 3, excluir, 4-listar todos os cadastrados, ao final da operação deve dar uma mensagem indicando o resultado da operação e perguntando se deseja realizar
# outra operação, o seu aplicativo apenas deve encerrar quando a opção não for inserida.

nomes = ['Francineide', 'Lucas', 'Matheus']


operacao = 'sim'

while operacao == 'sim':

    print('informe a ação desejada')
    print('1 Cadastra nome')
    print('2 Atualize nome')
    print('3 Exclua nome')
    print('4 Listar nomes')

    opcao = int(input('Informe a açao desejada'))

    match opcao:

        case 1:
            nome = input('que nome deseja cadastrar:')
            nomes.append(nome)
        case 2:
            nome = input('que nome deseja atualizar:')
            novo_nome = input('Qual será o novo nome?')
            
            nomes[nomes.index(nome)] = novo_nome
        case 3: 
            nome = input('que nome deseja remover?:')
            nomes.remove(nome)
        case 4: 
            for indice , nome in enumerate (nomes):
                print(f'{indice}-{nome}')
        case _:
            print('opção invalida')

    operacao = input('Deseja realizar outra operação? ').lower()

    if operacao != 'sim':
        break
