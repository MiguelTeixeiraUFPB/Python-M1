#usamos \033[x;y;zm
#para criar cores primeira casa indica a fonte q vai de 0 none ; 1 negrito; 4 underline
#segunda casa indica a cor sa fonte da númeração 30 a 37
#terceira casa indica cor de fundo de 40 a 47
nome=str(input('digite seu nome: '))
print('o seu nome é {} {} {}'.format( '\033[4;30;41m',nome,'\033[m'))
