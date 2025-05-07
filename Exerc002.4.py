'''Comece executando as instruções de atribuição:

>>> s1 = 'ant'
>>> s2 = 'bat'
>>> s3 = 'cod'
            
Escreva expressões Python usando s1, s2 e s3 e os
operadores + e * a fim de avaliar para:  

  
'ant bat cod'
ant ant ant ant ant ant ant ant ant ant'
'ant bat bat cod cod cod'
'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'
'batbatcod batbatcod batbatcod batbatcod batbatcod'''

s1 = 'ant'
s2 = 'bat'
s3 = 'cod'

print(s1, s2, s3)
print(10 * (s2 + ' '))
print(s1, 2 * (s2 + ' '), 3 * (s3 + ' '))
print(7 * (s1 + ' ' + s2 + ' '))
print(5 * (s2+s2+s3 + ' '))

'''1. s1 + ' ' + s2 + ' '
Isso junta(concatena) as strings:

s1 = "Olá"

' ' = um espaço

s2 = "mundo"

' ' = outro espaço no final

Resultado: "Olá mundo "

2. 7 * (...)
Multiplica a string resultante por 7.

Em Python, strings podem ser repetidas com * .

Resultado: "Olá mundo Olá mundo Olá mundo Olá mundo Olá mundo Olá mundo Olá mundo "

3. print(...)
Imprime a string repetida 7 vezes.
'''
