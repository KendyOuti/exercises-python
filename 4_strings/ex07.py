'''
Defina uma matriz de caracteres para guardar um texto para fazer um editor de texto 
que leia as várias linhas dadas pelo usuário e quando este digitar uma linha em 
branco, reescreva o texto do usuário e imprima as seguintes estatísticas do texto: 
número de caracteres digitados, número de espaços em branco e número de linhas. 
'''

paragrafo = []

cont_linhas = cont_branco = cont_caracteres = 0
while True:
    linha = []
    texto_linha = str(input(f"Linha {cont_linhas + 1}: ")).strip()
    if texto_linha == "":
        print()
        break
    else:
        linha.append(texto_linha)
        paragrafo.append(linha)
        cont_linhas += 1
        cont_branco += texto_linha.count(" ")
        cont_caracteres += len(texto_linha) - texto_linha.count(" ")

for linha in paragrafo:
    for palavra in linha:
        print(palavra)

print(f"Número de caracteres = {cont_caracteres}")
print(f"Número de espaços em branco = {cont_branco}")
print(f"Número de linhas = {cont_linhas}")