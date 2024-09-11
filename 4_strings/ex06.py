'''Faça um programa que leia uma frase e inverta todas as letras maiúsculas para 
minúsculas e vice-versa. Além disso, o programa deve colocar um hífen no lugar de 
todos os espaços em branco. '''

def inverter_case(frase):
    if (len(frase) == 0):
        return ""
    else:
        letra = frase[0]
        if letra.isalpha():
            letra = letra.swapcase()
        elif letra == " ":
            letra = "-"
        else:
            pass

        return letra + inverter_case(frase[1:])

def main():
    frase = str(input("Informe uma frase: "))
    resultado = inverter_case(frase)
    print(f"{resultado}")

main()