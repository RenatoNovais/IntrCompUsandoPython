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

    Se precisar de ajuda com algum deles ou quiser mais exercícios em algum tópico específico, é só avisar! 😊
'''
