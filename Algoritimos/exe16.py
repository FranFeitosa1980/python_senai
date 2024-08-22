# Desenvolva um programa que peça ao usuário um tipo de combustível (gasolina, etanol, diesel) e exiba o preço correspondente por litro.

combustivel = str(input('Informe um tipo de combustível:gasolina, etanol, diesel \n'))

if combustivel == 'gasolina':
    print('Valor da gasolina é de R$ 6,00')
elif combustivel == 'etanol':
    print('O valor do etanol é de R$ 4,00')
else:
    print('O valor do diesel é de R$ 6,50')
