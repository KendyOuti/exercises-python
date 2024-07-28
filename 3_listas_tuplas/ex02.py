'''
Escreva um programa que recebe como entrada um número inteiro positivo n. Em 
seguida, seu programa deve ler n números inteiros e adicioná-los em uma lista. Por
fim, seu programa receberá um número inteiro x e deve verificar se x pertence ou não à lista.
'''

inteiros = []
n = int(input("n = "))
print()

for c in range(n):
    inteiros.append(int(input()))

x = int(input("\nx = "))
print("\nx pertence a lista" if x in inteiros else "\nx não pertence a lista")
