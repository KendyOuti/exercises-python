'''
Sendo S = 1 - 1/2 + 1/3 - 1/4 + 1/5 - ... + 1/n, construa um programa que calcule e mostre o valor da série S.
'''

n = int(input())

s = 0

for c in range(1, n+1):
    if (c % 2 == 0):
        check = -1
    else:
        check = 1
    s = s + (check * (1 / c))

print(f"\n{s:.2f}")
