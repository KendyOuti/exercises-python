'''Faça um programa que conta quantos caracteres únicos existem em uma string. A 
string 'Hello, world!' tem dez caracteres únicos, enquanto a string 'zzz' tem apenas 
um. Utilize um dicionário para resolver esse problema.'''

def cont_caracteres(frase):
    contador = {}
    for letra in frase:
        contador[letra] = contador.get(letra, 0) + 1
    
    return len(contador)

def main():
    frase = str(input("Informe uma frase: "))
    resultado = cont_caracteres(frase)
    print(f"Quantidade de caracteres únicos: {resultado}")

main()
