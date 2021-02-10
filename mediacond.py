nota1=float(input('digite sua primeria nota: '))

nota2=float(input('digite sua segunda nota: '))

media=(nota1+nota2)/2

if media>=7:
    print('você foi aprovado com média {}'.format(media))
else :
    print('voê foi reprovado, sua média é de {}, estude mais para o próximo período'.format(media))    
