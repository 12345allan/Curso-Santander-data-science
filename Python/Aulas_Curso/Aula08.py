# Estrutura de listas:É uma estrutura de dados que consiste em que consegue armazenar varios tipos de variaveis distintos dentro dela
# Indexação é uma acessando um elemento por meio de indices, os indices no python começam pelo o 0, no python pode acessar o indice negativo
# Slices: pegar um pedaço da lista
#> Listas

# Antes
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# com lista
# Cochete no python significa a criação de listas
notas = [7.9, 9.4, 8.2]
# Criando listas
lista = [] # Lista vazia 
lista = list() # Lista vazia com o comando list()
lista = [26, 'Allan', 3.14159, False] # Lista no python aceita varios tipos de dados
lista_de_listas = [10,[1, 2, 3]] # Lista dentro de listas


# Indexação e Slices(fatiamento)

lista = [10, 'Allan', 3.1415, True]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])


# Slices = fatiamento 

lista = [10, 50, 30, 40, 25, 60, 5]

print(lista[0:3])
print(lista[3:6])
print(lista[3:])
print(lista[2:6:2])


#> Interação com For

# 1. Ultilizando os proprios elementos da lista

for elemento in lista:
    print(elemento)

# 2. Ultilizando os índices

print('Comprimento da lista:', len(lista))

for i in range(len(lista)):
    print(i)

# Continuação de listas

# > Métodos de Listas
# Método e uma "função" que esta atrelada a uma variavel

lista = [1, 3, 12, 8, 2]


# append
# adicionar um elemento no final de uma lista 

print('Antes do append:' ,lista)

lista.append(3)

print('Depois do append: ', lista)


# insert
# Adiciona um elemento numa lista podendo escolher a posição desse elemento

lista.insert(2, 10)

print('Depois do Insert: ', lista)

# extend
# O extend serve para vc juntar duas listas

lista2 = [1, 2, 3]
# Pega os elelmentos da lista2 e joga no final da lista
lista.extend(lista2)

print('Depois do extend: ', lista)
# pop
# Remove o elemento especifico ou se não especificar a posição ele vai remover o ultimo elemento

lista.pop()
# Eliminando o ultimo elemento da lista 
print('Lista depois do pop: ', lista)

# Eliminando do elemento do índice 0
lista.pop(0)
print('Depois da eliminação: ', lista)

# remove
# E dito qual e o elemento para ser removido da lista

# Removendo o indice 3, se tiver mais um indice igual ele remove o primeiro que achar
lista.remove(3)

print('Depois do remove: ', lista)

#count
# Contar quantas vezes um elemento aparece numa lista
# Imprimindo e passando a contagem do numero para a lista
print('Quantidade de 2 na lista: ', lista.count(2))

# index
# Me diz o indice de um determinado elemento na lista
# imprimindo e pedindo o indice do elemento
print('índice do elemento 12:', lista.index(12))


# short
# Serve para ordenar uma lista

# Ordenando decrecente:
lista.sort(reverse=True) # reverse=True e para ele ordenar decrecente 
# Imprimindo a lista decrecente
print(lista)

# Ordenando a lista crescente
lista.sort()

# Imprimindo a lista crescente
print(lista)

# Funções para as listas:

# len
# Para saberr quantos elementos tenho na lista

print(len(lista))
# sum
print(sum(lista)) # Somando todos os elementos da lista

# max

print('Maior elemento da lista: ', max(lista)) # Passando o maior elemento da lista

# min

print('Menor elemento da lista: ', min(lista)) # Passando o menor elemento da lista
