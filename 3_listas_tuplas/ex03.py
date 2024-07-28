'''
Faça um programa para calcular a média de um conjunto de 15 valores dados pelo 
usuário e armazenados em um vetor. Ao final, imprima a média e todos os valores 
digitados que ficaram abaixo da média.
'''

conjunto = []

for c in range(15):
    conjunto.append(int(input()))

media = sum(conjunto) / len(conjunto)

print(f"\n{media}\n")

for valor in conjunto:
    if valor < media:
        print(valor, end=' ')
    


