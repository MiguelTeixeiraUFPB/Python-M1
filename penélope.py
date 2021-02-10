diasmes=30
semana=7#ela n especificou essa variável
dia=int(input('digite a quantidade de dias vividos : '))#ela n colocou o tipo primitivo
ano=dia//365#ela colocou dias como 366 isso seria um ano bissexto
meses=dia//diasmes#divisões inteiras
semanas=dia//semana
print('você viveu aproximadamente {} anos'.format(ano))
print('você viveu aproximadamente {} meses'.format(meses))
print('você viveu aproximadamente {} semanas'.format(semanas))