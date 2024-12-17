# Estruturas condicionais
# As estruturas condicionais elas vão determinar se o trecho do codigo vai ser executado ou não 

idade = 20

if idade >= 18:
    print('Você é maior de idade.')
else: 
    print('Você e menor de idade.')

"""
 Imagine que você queia imprimir "Aprovado(a)", caso o estudante tenha uma 
 média superior ou igual a 7, e "Reprovado", caso a média seja inferioa 7.
"""

media = float(input('Informe a média do aluno:'))

if media >= 7:
    print('você foi aprovado(a)!')
elif media >= 5:
    print('Recuperação')
else:
    print('Você foi reprovado(a).')