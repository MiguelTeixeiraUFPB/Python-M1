ano=int(input('digite o ano para saber se ele é bissexto: '))

if ano % 4== 0 and ano % 100 != 0 or ano % 400 == 0:
    print('esse ano é bissexto')
else:
    print('não é bissexto')    