nome=input('qual seu nome: ')

#adicionando cores como variável
cores= {'final':'\033[m',
'azul':'\033[0;34m',
'amarelo':'\033[0;33m'} 

print('{} olá {}{}{} {}seja bem vindo{} !'.format(cores['amarelo'],
cores['azul'],nome,cores['final'],cores['amarelo'],cores['final']))
