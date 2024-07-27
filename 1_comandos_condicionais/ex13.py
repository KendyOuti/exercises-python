'''
Elabore um programa que receba três valores quaisquer e imprima o menor valor dos 
três lidos.
'''

num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

menor = num_1

if num_2 < menor:
    menor = num_2

if num_3 < menor:
    menor = num_3 

print(f"\n{menor}")


