nome=str(input('digite seu nome e sobrenome: ')).strip()#função .strip() tira os espaços antes e depois
print(len(nome))#me diz a quantidade de letras e espaços ocupado na memória
print(nome.upper())#tudo em maiúsculo
print(nome.title())#apenas primeira letra de cada palavra
print(nome.lower())#letras em minúsculo
print(nome.count(' '))#procura letras, espaços dentro da variavel
separa=nome.split()#serve para separar as palvras de forma q fia [0,1,2,3]
print('o seu primeiro nome é {} e tem  letras {} '.format(separa[0], len(separa[0])))
