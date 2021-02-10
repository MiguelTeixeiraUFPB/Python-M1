valorPago=int(input('digite o valor pago: '))
valorProduto=int(input('digite o valor do produto: '))
valorTroco = valorPago - valorProduto

troco5 = valorTroco // 5
troco2 = (valorTroco - (troco5*5)) // 2
troco1 = ((valorTroco - (troco5*5)) -troco2*2)//1

print ('valor troco',valorTroco)
print ('quantidade de notas de R$5 é ',troco5)
print ('quantidade de notas de R$2 é',troco2)
print ('quantidade de moedas de R$1 é',troco1)