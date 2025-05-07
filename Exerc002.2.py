'''A soma de 2 e 2 é menor que 4.
O valor de 7 // 3 é igual a 1 + 1.
A soma de 3 ao quadrado e 4 ao quadrado é igual a 25.
A soma de 2, 4 e 6 é maior que 12.
1387 é divisível por 19.
31 é par. (Dica: o que o resto lhe diz quando você
divide por 2?)
O preço mais baixo dentre R$ 34,99, R$ 29,95 e R$ 31,50
é menor que R$ 3,00.*'''
somaMenor = 2 + 2 < 4
print('A soma de 2 + 2 é menor que 4 =', somaMenor)
#===================================================
valorIgaul = 7 // 3 == 1+ 1
print('O quociente inteiro de 7 //3 é igual a 1 + 1: valor =', valorIgaul)
#===================================================
somaQuadrado = 3**2 + 4**2 == 25
print('A soma de 3 ao quadrado e 4 quadrado é igual a 25 =', somaQuadrado)
#===================================================
somaMaior = 2 + 4 + 6 > 12
print('A soma de 2,4 e 6 é maior que 12 =', somaMaior)
#===================================================
dividento = 1387
divisor = 19 
eh_divisivel= (dividento % divisor == 0)
print(f'O número {dividento} é divisível por {divisor} = {eh_divisivel}')
#====================================================
restoPar = 31 % 2 == 0
print('O número 31 é par',restoPar)
#====================================================
precoMin = min(34.99, 29.95,31.50) < 30.00
print('O menor preço entre R$34.99, R$29.95 e 31.50 é menor que R$30.00', precoMin)
