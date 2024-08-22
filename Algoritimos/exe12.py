# Escreva um programa que peça ao usuário para escolher um modo de transporte (carro, bicicleta, a pé) e exiba uma mensagem com a velocidade média correspondente.

transporte = str(input('Escolha um meio de transporte: carro, bicicleta, a pé: \n'))

if transporte == 'carro' :
    print('Sua velocidade média é de 60 km/h')

elif transporte == 'bicicleta' :
    print ('Sua velocidade média é de 25 km/h') 

else:
    print('Sua velocidade média é de 2 km/h')
