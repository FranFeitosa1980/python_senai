
# candidato = int(input('Informe o numero do candidato'))

# # if candidato == 13:
# #     print('Votou no Lula')
# # elif candidato == 22:
# #     print('Votou no Bolsonaro')
# # else:
# #     print('Candidato invalido')


#match case uma estrutura condicional 

# candidato = int(input('Informe o numero do candidato \n))
# match candidato:
#     case 13:
#         print('votou no Lula')
#     case 22:
#         print('votou no Bolsonaro')
#     case _:
#         print('opçao invalida')

        # atribuição de valores a uma variavel 

# numero=10
# print(numero)

# numero =numero+10
# numero +=10
# print(numero)

# numero = numero -10 
# numero -=10
# print(numero)

# numero = numero *10 
# numero *=10
# print(numero)

# numero = numero / 10
# numero /=10 
# print(numero)

# verificando se um numero é par ou impar 

# numero = int(input('Informe o numero'))

# if numero % 2 == 0:
#     print('numero par')

# else:
#     print('numero é impar')

# laços de repetição for em portgues 'para'

# for i in range (5):
#     print('Francineide')
#     print (i)

# nomes = ['Luciano', 'Lucas' , 'Arthur', 'Aline', 'Beatriz']

# print(nomes)

# for nome in nomes:
#     print(nome)

# frutas = ['banana', 'maçã' , 'morango', 'laranja']

# # for fruta in frutas:
# #     print(fruta)

# print(frutas[2])


# for indice, fruta in enumerate (frutas):
#     print(f'Suas frutas são {indice}: {fruta}')

# nomes = []

# for i in range(5):
#     nome = input('Informe seu nome: \n')
#     nomes.append(nome)

# print(nomes)
# for nome in nomes:
#     print(nome)

# nome = 'Luciano'

# for i in nome:
#     print(i)

# while em portugues: Enquanto 

# numero = None

# while numero !=0:
#     numero = int(input('Informe o numero\n'))

# contador = 1
# numero =int(input ('Informe o numero:'))

# while contador <10:
#     print(contador)
#     contador +=1

numero = 10
while True:
    numero *=10
    print(numero)
    if numero >10000000:
        break