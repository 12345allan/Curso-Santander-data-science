# > Função 

# 1. O que são funções e pq ultilizá -las?

# Funções são uma caixa preta algo que cria para usar na logica repetida vezes

# Funções que ja usamos anteriormente

"""print() # - Imprimi uma mensagem (int, float, str) no console(terminal, cmd)
input() # - Retorna um dado informado pelo o usuário (entrada padrão) e pode receber uma string
len() # - Recebe uma lista e retorna o tamanho dessa lista 
max() # - Retorna o maior valor de uma lista"""

# 2. Criação de Funções

#Função inicial
# def cria uma função 
def saudacao(): 
    print('Seja bem vindo(a)!')
    print('Olá, é um prazer ter você fazendo parte desse curso!')
# Chamando a função 
saudacao()

# Função com parâmetros
def saudacao(nome, curso): 
    print(f'Seja bem vindo(a), nome, {nome}!')
    print(f'Olá, é um prazer ter você fazendo parte desse curso de {curso}!')

saudacao('Allan', 'Phyton')


# Função com parâmetros default
# Dando um valor padrão ao parâmetro curso pelo default
def saudacao(nome, curso= 'Python'): 
    print(f'Seja bem vindo(a), nome, {nome}!')
    print(f'Olá, é um prazer ter você fazendo parte desse curso de {curso}!')

saudacao('Allan')

# Funções com retorno

def soma(num1, num2): 
    return num1 + num2

resultado = soma(5, 7)

print('O Resultado da soma é, ', resultado)

def calculadora(num1, num2, operacao='+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2

resultado = calculadora(10, 20, '-')

print(resultado)