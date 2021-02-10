velocidade=float(input("digite a atual velocidade do veículo: "))

if velocidade>80:
    multa=velocidade-80
    multavalor=multa*7
    print('\033[1;31mVocê ultrapassou o limite de velocidade, pague a multa de {:.2f}R$\033[m'.format(multavalor))   

print('Tenha um bom dia! E dirija com cuidado')    