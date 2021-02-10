from random import randint
from time import sleep

computador=randint(0,5)#essa função irá sortear um  número de 0 a 5

print('==x=='*15)
print('vou pensar em um número entre 0 e 5 tente adivinar')
print('==x=='*15)

jogador=int(input('qual número eu pensei?'))
print('processando')

sleep(3)

if computador==jogador:
    print('você acertou! o número que eu pensei foi:{}'.format(computador))
else:
    print('você errou, tente novamente, o número o qual pensei foi:{}'.format(computador))

