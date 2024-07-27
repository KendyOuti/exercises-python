'''
Faça um programa que calcule o Máximo Divisor Comum entre dois números. 
'''

num_1 = int(input())
num_2 = int(input())

if (num_1 % num_2 == 0):
    mdc = num_2
elif (num_2 % num_1 == 0):
    mdc = num_1
else:
    i = 1
    while (i < num_1) or (i < num_2):
        if num_1 % i == 0 and num_2 % i == 0:
            mdc = i
        i += 1

print(f"\n{mdc}") 

'''
OBS: Método mais eficiente: Algoritmo de Euclides
'''
