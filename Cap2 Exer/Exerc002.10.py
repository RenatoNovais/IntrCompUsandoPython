'''Escreva expressões Python correspondentes ao seguinte:


O comprimento da hipotenusa em um triângulo retângulo cujos
dois outros lados têm comprimentos a e b
O valor da expressão que avalia se o comprimento da hipotenusa
acima é 5
A área de um disco com raio a
O valor da expressão Booleana que verifica se um ponto com
coordenadas x e y está dentro de um círculo com centro
(a, b) e raio r
'''


import math

a, b = 4, 4  # Catetos
x, y = 1, 2  # Ponto
centro_a, centro_b = 0, 0  # Centro do círculo
raio = 5

# 1. Hipotenusa
hipotenusa = math.sqrt(a ** 2 + b ** 2)
print(f'Hipotenusa: {hipotenusa:.1f}')


# 2. Verificar se hipotenusa é 5
hipotenusa = math.sqrt(a ** 2 + b ** 2) == 5
print(f'Hipotenusa maior que 5: {hipotenusa == 5}')


# 3. Área do disco
area = math.pi * a ** 2
print(f'Área do disco: {area:.2f}')


# 4. Ponto dentro do círculo
dentro = math.sqrt((x - centro_a) ** 2 + (y - centro_b) ** 2) <= raio
print(f'Ponto dentro do círculo? {dentro}')

