'''
A série de Fibbonacci é gerada da seguinte forma: os dois primeiros termos são 1, os demais são dados pela soma dos dois anteriores. Faça um programa que imprima os “n” primeiros termos da série, sendo “n” dado pelo usuário.
'''

n = int(input()) #numeros de termos

f_1 = f_2 = 1

print(f"{f_1} {f_2}", end= ' ')

for c in range(2, n):
    f_3 = f_1 + f_2
    f_1 = f_2
    f_2 = f_3
    print(f"{f_3}", end = ' ')

