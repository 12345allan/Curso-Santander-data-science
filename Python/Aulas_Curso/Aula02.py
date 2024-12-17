# Variáveis 
# O que são variáveis: São pedaços da memoria que você está reservando para guardar uma informação 
# Toda variável tem um nome
# O comando type diz o tipo da variável
# E possivel imprimir varias variáveis usando a virgula para separa-las

# 1. Variáveis

idade = 26 # Criando uma variável

print(idade)

nome = "Allan Richard"

print(nome)

"""
 Tipos de variáveis

 1. int: números inteiros, ou seja, números sem parte decimal: 0, 5, -1, 1000
 2. float: números reais, ou seja, números com partes decimal: 1.0, -2.7, 3.14
 3. str : cadeias de caracteres, ou seja dados textuais(string)
 4. boll: valores lógicos (booleanos): True e False  
"""

idade = 26
altura = 1.77
nome = "Allan Richard"
estudando = 'java'

print(type(idade))
print(type(altura))
print(type(nome))
print(type(estudando))

# Obtendo dados do usuário e salvando em variáveis
linguagem = input("Qual é a linguagem de programação quw vc está estudando? ")
# Imprimindo a linguagem
print('A linguagem de programação que você está estudando é', linguagem)


nome = input('Qual e o seu idade:')
nome = input('Qual e a sua altura:')
nome = input('Qual e o seu nome:')
nome = input('estuda oque:')

print('Qual é a sua idade, altura, nome e oque estuda: ', nome, altura, nome, estudando)