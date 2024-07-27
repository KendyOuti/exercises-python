'''
Escreva um programa que, dados três números inteiros, imprima os números em 
ordem crescente.
'''

num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

if num_1 > num_2:
    num_2, num_1 = num_1, num_2

if num_2 > num_3:
    num_3, num_2 = num_2, num_3 

if num_1 > num_2:
    num_2, num_1 = num_1, num_2  

print(f"\n{num_1} {num_2} {num_3}")




    