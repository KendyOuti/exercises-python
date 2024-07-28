'''
Seja o polinômio: P(X) = anXn + an-1Xn-1 + an-2Xn-2 + .... + a1X + a0
Escreva um programa que leia um número real x, a ordem do polinômio n (no máximo 
20), os coeficientes ai e calcule o resultado. Imprima o polinômio lido e o valor 
calculado. 
'''

n = -1
while n < 0 or n > 20:
    n = int(input("n = "))

x = int(input("x = "))

coeficientes = [] 
resultado = 0
for c in range(0, n+1):
    coef = int(input(f"Coeficiente a{c} = "))
    coeficientes.append(coef)
    resultado = resultado + ((coef) * (x ** c)) 



