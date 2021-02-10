from math import sqrt
cata=float(input('qual o valor do cateto adjacente?'))
cato=float(input('qual o valor do cateto oposto'))
c=(cata*cata)+(cato*cato)
hip=sqrt(c)

print( ' a hipotenusa desse triangulo retangulo é: {:.2f}'.format(hip))

