nome=str(input('digte seu nome:')).upper().strip()
print( 'seu nome possui {} letras A'.format(nome.count('A')))
print('ele aparece na posição {}'.format(nome.find('A')+1))#find diz a posição em que está
print('ele aparece pela última vez na posição{}'.format(nome.rfind('A')+1))

