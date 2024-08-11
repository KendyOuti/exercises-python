'''
Um palíndromo é uma palavra ou frase que pode ser lida da mesma forma tanto da 
esquerda para a direita como da direita para a esquerda (desconsiderando os 
espaços em branco). Considere que a entrada não possui sinais de pontuação ou 
acentos. Escreva um programa que, dada uma String, verifique se ela é um 
palíndromo.
Ex. Palíndromos = A cara rajada da jararaca; Roma me tem amor; Anotaram a data da maratona
'''

texto_original = str(input("")).lower().split()

texto_limpo = ''.join(texto_original)
texto_invertido = texto_limpo[::-1]

if texto_limpo == texto_invertido:
    print("A frase é um palíndromo")
else:
    print("A frase não é um palíndromo")
