from random import choice
n1=str(input('nome do primeiro aluno: '))
n2=str(input('nome do segundo aluno: '))
n3=str(input('nome do terceiro aluno: '))
lista=[n1,n2,n3]
escolhido=choice(lista)
escolhido2=choice(lista)
escolhido3=choice(lista)
print('o aluno escolhido para cor azul é {}{}{}'.format('\033[0;34m',escolhido,'\033[m'))
print('o aluno escolhido para cor vermelha é {}{}{}'.format('\033[0;31m',escolhido2,'\033[m'))
print('o aluno escollhido para cor verde é {}{}{}'.format('\033[0;32m',escolhido3,'\033[m'))