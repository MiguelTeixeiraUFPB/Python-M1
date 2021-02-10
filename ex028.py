from random import randint #biblioteca random, e opção randint
from time import sleep

sorteio= randint(0,999)

print('xx<>xx' *10)#decoração
print('\033[1;31m pensei em um número, vamos ver se você advinha \033[m')#adicionei a cor vermelha
print('xx<>xx' *10)#decoração

num=int(input('digite um número: '))

print('\033[1;34m processando... \033[m ')#adicionei a cor azul com o tipo de fonte 1

sleep(3)#da um atraso de 3 segundos para mostrar oq vem depois

if num==sorteio:
    print('você acertou o número pensado foi {}'.format(sorteio))
else:
    print('você errou, o número pensado não foi {}'.format(num))    
print()    