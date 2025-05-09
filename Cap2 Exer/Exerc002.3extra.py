'''
# **Exercícios Adicionais sobre Strings**

# **1. Manipulação Básica de Strings**
a) Escreva um programa que peça ao usuário para digitar seu nome e sobrenome separadamente. Depois, concatene-os em uma única string e imprima:
    - O nome completo.
   - O nome completo em maiúsculas.
   - O nome completo em minúsculas.
   - O número de caracteres no nome completo(sem contar espaços).

'''
nome = input('Digite seu nome: ')
sobreNome = input('Digite seu sobrenome: ')
nomeCompleto = nome + ' ' + sobreNome
# usado f-string para imprimir as expressão atrinbuída as variáveis do input
print(f'Seu nome completo é {nomeCompleto}')
# .replace(" ", "") → Remove o espaço, resultando em "RenatoNovais".
nomeCompletoSemEspaco = nomeCompleto.replace('', '')
print(len(nomeCompletoSemEspaco))
# len() → Conta os caracteres restantes(9).



'''

    b) Escreva um programa que peça uma frase ao usuário e imprima:
   - A primeira letra de cada palavra em maiúscula.
   - A frase invertida(de trás para frente).
   - Quantas vezes a letra "a" aparece(maiúscula ou minúscula).
    ---

    
    #### **2. Fatiamento (Slicing) de Strings**
    a) Dada a string `s = "ProgramaçãoPython"`, faça:
   - Imprima os 5 primeiros caracteres.
   - Imprima os últimos 4 caracteres.
   - Imprima do 3º ao 8º caractere.
   - Imprima a string pulando de 2 em 2 caracteres(ex.: "Pormçãotn").

    b) Escreva um programa que peça uma palavra ao usuário e:
   - Imprima apenas as letras nas posições pares(ex.: "Python" → "Pto").
   - Imprima a palavra sem a primeira e a última letra(ex.: "Computação" → "omputaçã").

    ---

    #### **3. Operações com Strings**
    a) Dada a string `frase = "Python é incrível!"`, faça:
   - Substitua "incrível" por "poderoso".
   - Verifique se a palavra "Python" está na frase.
   - Divida a frase em uma lista de palavras.

    b) Escreva um programa que peça uma senha ao usuário e verifique se:
   - A senha tem pelo menos 8 caracteres.
   - Contém pelo menos um número.
   - Contém pelo menos uma letra maiúscula.

    ---

    #### **4. Formatação de Strings**
    a) Crie uma string formatada que mostre o resultado da expressão `3 * 5 + 2` no formato:
   `"3 * 5 + 2 = 17"` (use f-strings).

    b) Peça ao usuário para digitar seu nome, idade e cidade. Imprima uma mensagem formatada como:
   `"Olá, [Nome]! Você tem [Idade] anos e mora em [Cidade]."`

    ---

    #### **5. Desafios**
a) ** Palíndromo**: Escreva um programa que verifique se uma palavra é um palíndromo (igual de trás para frente, como "arara").

b) ** Criptografia simples**: Crie um programa que substitua cada letra de uma palavra pela próxima no alfabeto (ex.: "abc" → "bcd", "z" → "a").

    ---

    Esses exercícios cobrem conceitos como:
    - Concatenação e métodos de strings (`upper()`, `lower()`, `replace()`, `split()`).
    - Fatiamento (`slicing`).
    - Formatação (`f-strings`).
    - Verificação de condições em strings.    
'''


#=====================Exercícios com Operadores de String===============================


'''1. Operador in (verificação de substring)
Exercício 1:
Escreva um programa que verifique se a palavra "sol" está presente na string "O sol é brilhante hoje." e imprima o resultado(True ou False).
'''
string = 'O sol é brilhante hoje'
substring = 'sol'
resultado = substring in   string
print(resultado)

'''Exercício 2:
Crie uma função que receba uma string e uma substring como parâmetros, e retorne True se a substring existir na string, caso contrário, retorne False. Teste com a string "Python" e a substring "tho".
'''




'''
2. Operador not in (negação de substring)
Exercício 1:
Verifique se a palavra "chuva" não está presente na string "Hoje o dia está ensolarado." e imprima o resultado.

Exercício 2:
Peça ao usuário para digitar uma frase e uma palavra. O programa deve informar se a palavra não está na frase (usando not in).

3. Concatenação(+)
Exercício 1:
Concatene as strings "Hello" e "World!" com um espaço entre elas e imprima o resultado("Hello World!").

Exercício 2:
Peça ao usuário para digitar seu nome e sobrenome separadamente. Concatene-os em uma única string e imprima: "Seu nome completo é [nome completo]".

4. Repetição(*)
Exercício 1:
Imprima a string "abc" repetida 3 vezes usando o operador * .

Exercício 2:
Crie uma função que receba um número n e imprima uma "borda" composta por n vezes o caractere "-". Por exemplo, para n = 5, a saída deve ser "-----".

5. Indexação(s[i])
Exercício 1:
Dada a string "programação", imprima o terceiro caractere(índice 2).

Exercício 2:
Peça ao usuário para digitar uma palavra e um número inteiro i. Imprima o caractere no índice i da palavra(tratando casos em que i é inválido).

6. Função len()(comprimento da string)
Exercício 1:
Calcule e imprima o comprimento da string "OpenAI".

Exercício 2:
Peça ao usuário para digitar uma senha. Verifique se a senha tem pelo menos 8 caracteres usando len(). Se não tiver, imprima "Senha muito curta!".
'''