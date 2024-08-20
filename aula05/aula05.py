# numero1 = 10
# numero2 = 10

# print(numero1 > numero2)
# print(numero2 > numero1)

# # operador menor
# print (numero1 < numero2)
# print (numero2 < numero1)

# print(numero1 == numero2)
# print(numero1 >= numero2)
# print(numero1 <= numero2)
# print(numero1 != numero2)

# idade = int(input('Informe sua idade: \n'))

# if(idade > 120):
#     print('idade invalida')
# elif(idade >= 18):
#     print('maior de idade')
# elif(idade <0):
#     print ('ainda não nasceu')
# else:
#     print('menor de idade')


# idade = int(input('Informe sua idade: \n'))


# if(idade >=18):
#     print('Pode assistir o filme')
# elif(idade >=16):
#     acompanhado = input('Está acompanhado de adulto sim ou não? \n')
#     if(acompanhado == 'sim'):
#         print('Pode assistir')
#     else:
#         print('não pode assitir')
# else:
#     print('não pode assistir') 

# idade = int(input('Informe sua idade: \n'))

# if(idade <18):
#     acompanhado=input('Está acompanhado de adulto sim ou não? \n')
#     if ( acompanhado == 'sim'):
#         print('pode assistir')
#     else:
#         print('não pode assistir')
# else: 
#     print('pode assistir')

# alladin = input('Alladin apareceu? \n')
# jasmine = input('Jasmine apareceu? \n')

# if(alladin == 'sim') and (jasmine == 'sim'):
#     print('Love a noite toda')
# else:
#     print('Não rolou encontro')    

# 

alladin = input('Alladin apareceu? \n')
jasmine = input('Jasmine apareceu? \n')

if not ((alladin == 'sim') or (jasmine == 'sim')):
    print('Love a noite toda')
else:
    print('Não rolou encontro')  