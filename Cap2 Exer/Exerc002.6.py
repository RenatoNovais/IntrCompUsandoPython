'''Primeiro, execute a atribuição
palavras = ['taco', 'bola', 'celeiro', 'cesta', 'peteca']
Agora, escreva duas expressões Python que são avaliadas, respectivamente,
como a primeiro e a última palavras em palavras(min,max), na ordem do dicionário.
sorted(organiza a lista em ordem alfabética)
'''
palavras = ['taco', 'bola', 'celeiro', 'cesta', 'peteca']
coisas = [1, 'um', [1, 2, 'r']]
coisas.append(22)
coisas.remove(22)
palavras.append('gato')
contido = 'gato' not in palavras  # verifica se gato está na lista ou foi inlcuído
print(palavras + coisas)
print(palavras[0])
print(contido)
print(min(palavras))
print(max(palavras))
print(sorted(palavras))  # organiza a lista em ordem alfabética
print(len(palavras))  # mostra o tamanho da lista 5 caracteres
print(coisas.count(22))

