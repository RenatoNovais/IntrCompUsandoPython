'''Primeiro, execute a atribuição
palavras = ['taco', 'bola', 'celeiro', 'cesta', 'peteca']
Agora, escreva duas expressões Python que são avaliadas, respectivamente,
como a primeiro e a última palavras em palavras(min,max), na ordem do dicionário.
sorted(organiza a lista em ordem alfabética)
'''
palavras = ['taco', 'bola', 'celeiro', 'cesta', 'peteca']
palavras.append('gato')
contido = 'gato' not in palavras  # verifica se gato está na lista ou foi inlcuído 
print(palavras[0])
print(contido)
print(min(palavras))
print(max(palavras))
print(sorted(palavras))  # organiza a lista em ordem alfabética
print(len(palavras))  # mostra o tamanho da lista 5 caracteres