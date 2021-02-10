valor=float(input('quanto de dinheiro o senhor possui?R$ '))
rosa=5.80
trocorosa=valor-rosa
qntdrosa=int(valor//rosa)
#tulipa
tulipa=7.20
qntulipa=float(valor//tulipa)
trocotulipa=valor-qntulipa


if valor>=float(5.80):#condição rosa
    print('com o valor de {}R$ você poderá comprar {} rosa, e receberá {:.2f}R$ de troco'.format(valor,qntdrosa,trocorosa))
else:
    print('com o valor de {}R$ você não poderá comprar nenhuma rosa '.format(valor))

if valor>=float(7.20):#condição tulipas
     print('ou')
     print('com o valor de {}R$ você poderá comprar {} tulipa, e receberá {:.2f}R$ de troco'.format(valor,qntulipa,trocotulipa))
else:
     print('com o valor de {}R$ você não poderá comprar nenhuma tulipa'.format(valor))
print('Fim!')