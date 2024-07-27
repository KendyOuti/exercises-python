'''
Elabore um programa que calcule e mostre o fatorial de um número (N!), sendo que N é fornecido pelo usuário.
'''

n = int(input()) #Recebe o fatorial que deseja calcular

f = 1
for c in range(1,n+1):
    f = f * c

print(f)

