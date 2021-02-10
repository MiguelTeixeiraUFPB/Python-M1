from random import shuffle

n1=str(input('digite o nome do primeiro aluno:'))
n2=str(input('digite o nome do segundo aluno:'))
n3=str(input('digite o nome do terceiro aluno:'))

lista=[n1,n2,n3]

shuffle(lista)

print('\033[0;31ma ordem de apresentação é :\033[m')

print(lista)
