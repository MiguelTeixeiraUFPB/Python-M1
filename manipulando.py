nome=str(input('digite seu nome completo:')).strip()
print('seu nome em maiúsculo é {}'.format(nome.upper()))
print('seu nome em minúsculo é {}'.format(nome.lower()))
print('o seu nome tem {} letras'.format(len(nome)-nome.count(' ')))