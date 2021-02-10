#calculando quantidade cédulas de troco com 5,2 e 1 real em caixa.

valorcliente=int(input('valor da cédula do cliente : '))

precoproduto=int(input('preço produto: '))

troco=valorcliente-precoproduto

ced=5
totalced=0

while True:
    if troco>=ced:
     troco-=ced
     totalced+=1
    else:
        print('total de {} cédulas de {}R$'.format(totalced,ced))
        if ced==5:
            ced=2
        elif ced==2:
            ced=1
        if troco==0:
         break