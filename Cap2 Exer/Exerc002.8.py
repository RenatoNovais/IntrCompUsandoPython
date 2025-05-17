#================================================
'''
Regras de precedência em Python  A ordem de execução segue as regras de precedência de operadores em Python:
Parênteses (sempre têm a maior precedência)
Operadores aritméticos (+, -, *, /, etc.)
Operadores de comparação (==, !=, >, <, >=, <=)
Operadores lógicos (not, and, or - nesta ordem)'''
# ==============================================

'''Em que ordem os operadores nas expressões a seguir são avaliados?
2 + 3 == 4 or a >= 5
lst[1] * -3 < -10 == 0
(lst[1] * -3 < -10) in [0, True]
2 * 3**2
4 / 2 in [1, 2, 3]'''

a = 6  # Vamos definir um valor para 'a' para exemplo

# Expressão original
resultado = 2 + 3 == 4 or a >= 5

# Demonstração passo a passo
passo1 = 2 + 3          # Primeiro passo: adição
print(f"Passo 1: 2 + 3 = {passo1}")

passo2 = passo1 == 4     # Segundo passo: comparação de igualdade
print(f"Passo 2: {passo1} == 4 → {passo2}")

passo3 = a >= 5          # Terceiro passo: comparação maior ou igual
print(f"Passo 3: {a} >= 5 → {passo3}")

passo4 = passo2 or passo3  # Quarto passo: operador lógico OR
print(f"Passo 4: {passo2} or {passo3} → {passo4}")

print("\nResultado final:", resultado)

