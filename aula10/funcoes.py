# 

# numero1 = int(input('Informe o numero:'))
# numero2 = int(input('Informe o numero:'))

# print('A soma é:' , numero1 + numero2)


# numeros = [1,5,8,10,3,78,100,51]

# print(max(numeros))
# print(min(numeros))
# print(len(numeros))
# print(sum(numeros))

# media = sum(numeros)/len(numeros)
# print(media)

####### recebe uma lista e calcula a media 

# def media(numeros):
#     resultado = sum(numeros)/len(numeros)
#     return resultado

# # print (media(numeros))


# ####### função recebe dois numeros e soma 

# def soma (numero1, numero2): 
#     soma = numero1 + numero2
#     return soma

# ###### uso da função soma 

# print(soma (15,35))


# # ##### função sem retorno

# # def saudacao (nome):
# #     print(f'Ola {nome}')

# # #### uso da função 
# # saudacao('Fran')


# ## função com paramentro opcional 

# # def ola(nome, mensagem = 'Olá'):
# #     print(mensagem , nome)
# # ola('Francineide', 'oi')
# # ola ('Francineide')

# ### função com multiplo retorno


# # def dividir (numero1, numero2):
# #     resposta = numero1 // numero2
# #     resto = numero1 % numero2
# #     return resposta, resto

# # divisao, resto_divisao = dividir (9,2) 
# # print(divisao)
# # print(resto_divisao)


# ##### função 
# # numeros = [1,5,8,10,3,78,100,51]
# # print(type(numeros))
# # print(type[numeros])

# #### funçao lambda / forma abreviada de escrever uma função em apenas uma linha 

# from mailbox import NotEmptyError


# somar = lambda a, b: a+b
# print(somar (10,5))

# ###### função que recebe parametros indeterminados 

# def exibir_informacoes(*args):
#     print('Argumentos posicionais:' , args)

# exibir_informacoes(1,4, 'Francineide', 'Teste')


# def exibir_informacoes2(**args):
#     print('Argumentos posicionais:' , args)

# exibir_informacoes2(nome='Francineide', idade=44 , curso= 'Python')


#### dicionario / json em outras linguagens 
### key = value
### chave = valor 

pessoas = [{
    'nome':'Francineide', 
    'idade': 44, 
    'estado_civil': 'divorciada',
    'escolaridade': 'especialista'
}, 
{
    'nome':'Luciano', 
    'idade': 30, 
    'estado_civil': 'casado',
    'escolaridade': 'superior'
}]

print(pessoas[1])