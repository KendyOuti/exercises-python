'''
Escreva um programa que, dadas duas datas, determine qual delas ocorreu 
cronologicamente primeiro. Para cada uma das duas datas, leia três números 
referentes ao dia, mês e ano, respectivamente.
'''

print("\tData 1")
dia_1 = int(input("Dia: "))
mes_1 = int(input("Mês: "))
ano_1 = int(input("Ano: "))

print("\n\tData 2")
dia_2 = int(input("Dia: "))
mes_2 = int(input("Mês: "))
ano_2 = int(input("Ano: "))

if ano_1 < ano_2:
    print("\nData 1 ocorreu primeiro")
elif ano_1 > ano_2:
    print("\nData 2 ocorreu primeiro")
else:
    if mes_1 < mes_2:
        print("\nData 1 ocorreu primeiro")
    elif mes_2 < mes_1:
        print("\nData 2 ocorreu primeiro")
    else:
        if dia_1 < dia_2:
            print("\nData 1 ocorreu primeiro")
        elif dia_1 > dia_2:
            print("\nData 2 ocorreu primeiro")
        else:
            print("\nDatas iguais")
