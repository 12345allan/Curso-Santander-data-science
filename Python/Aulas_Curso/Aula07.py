# for: uma estrutura que permite criar repetições de forma controlada, quantas vezes eu quiser repeitr um techo de codigo
# Range aceita até 3 parametros

# Criação laço for, definição de faixa 10
#for variavel in range(10):
    #print(variavel)


# Range aceita até 3 parametros; range com 2 parametros (1,10), ele começa do 1 e vai até o menor que 10
"""for variavel in range(1, 10):
    print(variavel)"""


# For com 3 parametros: 
"""for variavel in range(1, 12, 3):
    print(variavel)"""

soma = 0

for i in range(1, 4):
    nota = float(input(f'Informe sua nota: {i}: '))
    # Variavel acumuladora:
    soma = soma + nota 
# saida pro usuario com uma divisão por 3:
print(soma / 3)