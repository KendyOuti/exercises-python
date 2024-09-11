'''Escreva um programa que conta todas as vogais presentes no texto recebido como 
parâmetro e retorna um dicionário contendo a quantidade de cada vogal. Seu 
programa deve exibir, no fim, os dados do dicionário retornado.'''

def cont_vogais(frase):
    frase = frase.lower()
    vogais = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    for letra in frase:
        if letra in vogais:
            vogais[letra] = vogais.get(letra, 0) + 1
    
    return vogais

def main():
    frase = str(input("Informe uma frase: "))
    resultado = cont_vogais(frase)
    for c, v in resultado.items():
        print(f"{c} = {v}")
    
main()
