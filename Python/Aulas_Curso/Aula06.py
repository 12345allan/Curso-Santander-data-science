# Laços de Repertição while
# o while do inglês e: enquanto
# O laço de repetição while enquanto uma determinada ação for satisfeita continua executando e quando não for mais satisfeita interrompe

numero_sorteado = 15

numero_escolhido = int(input('Informe um número entre 1 a 20: '))

while numero_escolhido != numero_sorteado:
    print('Você errou o número, tente novamente....')

    numero_escolhido = int(input('Informe um número entre 1 a 20: '))

print('Parabéns! Você acertou!')

# Exemplo 02: Estrutura com contador

contador = 0


while contador < 10:
    print(contador)

    contador = contador + 1