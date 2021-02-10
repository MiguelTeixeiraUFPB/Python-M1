#uso do quebra linha  \n
nome=str(input('qual seu nome?'))
idade=int(input('qual sua idade?'))
print("Seu nome é {}  \ne sua idade é {}".format(nome,idade))
#uso da continuação ,end=''
print('Bem vindo {}'.format(nome),end=" ")
print('sua idade é {}'.format(idade))
#uso do limitador de caracters {:.0f}  ou {:.1f} o número indica a quantidade de pontos float
n1=5/2
print('{:.0f}'.format(n1))
