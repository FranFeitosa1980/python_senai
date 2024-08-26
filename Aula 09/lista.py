
# cavaleiros = ['Seya', 'Aldebaran', 'Aldebaran', 'Shun', 'Shiryu', 'Yoga']

# print(cavaleiros)

# # append adiciona um novo elemento ao final da lista
# cavaleiros.append('Ikki')

# print(cavaleiros)

# # extend extende a lista com outra lista ao final da lista 

# cavaleiros.extend(['Shina', 'Maryn'])
# print(cavaleiros)

# # inserir na lista em uma posição especifica 

# cavaleiros.insert(0, 'Atena')
# print(cavaleiros)

# # remove, exclui um elemento pelo valor . Se houver ocorrencias repetidas, ele vai excluir apenas o primeiro


# cavaleiros.remove('Shun')
# print(cavaleiros)

# # pop - exclui o ultimo elemento da lista ou o indice informado


# elemento = cavaleiros.pop()
# cavaleiros.pop(0)
# print(cavaleiros)
# print(elemento)

# # index - retorna o indice da primeira ocorrencia de um valor procurado 

# print(cavaleiros.index('Yoga'))

# cavaleiros.pop(cavaleiros.index('Yoga'))
# print(cavaleiros)

# # alterando o valor de um elemento na lista

# cavaleiros[cavaleiros.index('Ikki')] = 'Ikki de fenix'
# print(cavaleiros)

# # contabilizando quantidade de elementos repetidos 
# print(cavaleiros.count('Aldebaran'))

# sort ordena a lista na ordem crescente 

frutas =['morango', 'maçã', 'abacaxi', 'kiwi', 'amora', 'umbu', 'laranja', 'bergamota']

numeros = [9,5,81,100,33,21,2]

frutas.sort()
numeros.sort()

print(frutas)
print(numeros)

frutas.reverse()
numeros.reverse()
print(frutas)
print(numeros)

del frutas[0]
print(frutas)

frutas.clear()
print(frutas)