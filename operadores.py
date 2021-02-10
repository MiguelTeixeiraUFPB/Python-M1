#operadores aritiméticos 
# (+) Adição
n1=5
n2=2
s=n1+n2
print('a soma de {} e {} é {}' .format(n1,n2,s))
# subtração (-)
s1=n1-n2
print('a subtração entre {} e {} é'.format(n1,n2,s1))
#multiplicação (*)
m=n1*n2
print('a multiplicação entre {} e {} é'.format(n1,n2,m))
#divisão(/)
d=float(n1/n2)
# Usamos o tipo primitivo (float) pois o o resultado da / é um número Real
print('a divisão entre {} e {} é {}'.format(n1,n2,d))
#divisão inteira (//)
d1=int(n1//n2)
print('a divisão inteira entre {} e {} é {}'.format(n1,n2,d1)) 
#Modulo ou resto da divisão(%)
d2=5%2
print('o resto de {} dividido por 2 é {}'.format(n1,n2,d2))
#potencia (**)
p=n1**n2
print('{} elevado a {} é {}'.format(n1,n2,p))
#Raiz quadrada **(1/2)
n1=81
r=n1**(1/2)
print("a raiz do número {} é {}".format(n1,r))
########Ordem de procedência 
#1- ()
#2- **
#3- *, /, //, %
#4- + e -
