nota1=float(input('digite sua primeira nota: '))
nota2=float(input('digite sua segunda nota: '))
media=(nota1+nota2)/2
if media>=7:
    print('o aluno foi aprovado com média {:.1f}',format(media))
else:
    print('aluno foi reprovado com média {:.1f}'.format(media))




