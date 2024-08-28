#  Desenvolva um programa que pergunte ao usuário quantas vezes ele quer que uma mensagem seja exibida, e depois use um for para imprimir essa mensagem repetidas vezes.

mensagens = str(input('Digite uma mensagem: \n'))
numero= int(input('Digite quantas vezes você quer que a mensagem apareça:\n'))

for i in range(numero):
    print(mensagens)
