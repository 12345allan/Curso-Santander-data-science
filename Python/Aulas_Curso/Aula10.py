# > Dicionarios

#Criando dicionarios

lista = {}
dicionario = dict()

dicionario = { 'nome': 'Allan', 'idade': '23', 'altura': 1.77 }

print(dicionario)
print(dicionario['idade'])


# Adicionando elementos em um dicionario

dicionario['Programador'] = True

print(dicionario)

dicionario['altura'] = 2

print(dicionario)

# Interando sobre um dicionario
#Percorrendo as chaves do dicionario
for chave in dicionario:
    # Imprimindo a cahve e o seu valor
    print(chave, dicionario[chave])

# Testando a existencia de uma chave
# vendo a chave peso se está dentro de dicionario
print('peso' in dicionario)
# Vendo a chave altura está demtro do dicionario
print('altura' in dicionario)