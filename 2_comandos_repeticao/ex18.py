'''
O número 3025 possui a interessante característica: 
30 + 25 = 55
552 = 3025
Faça um programa que procure todos os números de 4 algarismos que possuem essa 
característica. 
'''

for c in range(1000, 10000): #loop para analisar todos os números de 4 algarismos(1000 até 9999)
    soma = (c // 100) + (c % 100)

    # c // 100 = pega os 2 algarismos da esquerda
    # c % 100 = pega os 2 algarismos da direita 

    if (soma ** 2) == c:
        print(c, end=' ')


