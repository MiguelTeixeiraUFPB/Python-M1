#fatiamento de string
frase='miguel'
#espaços em branco também ocupam espaços na memória
print(frase[0:6])
#fatiando de outro modo
print(frase[:6])
#manipulando string
frase2='curso em video python'
print(frase2[0:21])
print(frase2[:14])
print(frase2[0:])
#analisando
#número de letras len(x)
print(len(frase))
#número de letras especificas x.count('letra')
print(frase.count('m'))
print(frase2.count('o',0,14))#x.count com fatiamento
print(frase2.find('deo'))#x.find('letras') onde inicia
print("curso"in(frase2))#frase in(x)
#substituição
print(frase2.replace('python','android'))
print(frase2.upper())
print(frase2.lower())
print(frase2.capitalize())#só o primeiro caractere fica maiúsculo
print(frase2.title())#a primeira letra de cada palavra em maiúsculo
print(frase2.strip())#elimina espaços no inicio e no final 
print(frase2.split())
print('-'.join(frase2))
#texto longo
print("""  Minha terra tem palmeiras,
Onde canta o Sabiá;
As aves, que aqui gorjeiam,
Não gorjeiam como lá                                                 
 .""")

















