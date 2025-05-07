'''A soma dos 5 primeiros inteiros positivos.
A idade média de Sara (idade 23), Mark (idade 19) e
Fátima (idade 31).
O número de vezes que 73 cabe em 403.
O resto de quando 403 é dividido por 73.
2 à 10ª potência.
O valor absoluto da distância entre a altura de Sara
(54 polegadas) e a altura de Mark (57 polegadas).
O menor preço entre os seguintes preços: R$ 34,99,
R$ 29,95 e R$ 31,50 '''

# ================================================================
valores = 1 + 2 + 3 + 4 + 5
print('A soma dos 5 primeiros números positivos são:', valores)
# =================================================================
IdMark = 19
idFatima = 31
idSara = 23

idMedia = (idFatima + idSara + IdMark) / 3
print(idMedia, 'É a média de idaded dos três')
# =================================================================
nuVezes = 403 // 73
print('O número de vezes que o número 73 cabe em 403 é :', nuVezes)
# =================================================================
rest = 403 % 73
print('O resto da divisão de 403 por 73 é:', rest)
# =================================================================
pot = (2**10)
print('A potência de 2 elevado a 10 é : ', pot)
# =================================================================
valorAbs = abs(54 - 57)
print('O valor absoluto entre a diferença de altura entre Sara (54 polegadas)  e MArk (57 polegadas) é :', valorAbs)
#=================================================================
menorPreco = min(34.99, 29.95, 31.50)
print('O menor preço entre os valores R$34.99 R$29.95  R$31.50 é:\n', menorPreco)
