print(3 != 1)
print(5 == 5)
print(13 % 10 != 3)
print(1 > 3 or 1 + 3 > 2)  # Or aceita pelo menos 1 verdadeira
print(1 > 3 and 1 + 3 > 2)  # conectivo and as duas precisão ser verdadeiras
print(not 1 > 3 and 1 + 3 > 2)

# =====================================================================================

celsius = eval(input('Quantos graus em Celsius? '))
kelvin = celsius + 273.15
fahrenheit = 1.8 * celsius + 32
print(celsius, 'graus Celsius  em Fahrenheit é :', fahrenheit, 'e em Kelvin é:', kelvin)
