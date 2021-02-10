#utilizando módulos de python importando biblioteca inteira

import math

#biblioteca mtmática

n1=int(input('digite um número :'))

raiz=math.sqrt(n1)

print('a raiz do número {} é {:.1f}'.format(n1,math.ceil(raiz)))

#>>>>para importar partes da biblioteca

from math import sqrt
#>>>>importando apenas a função de raiz quadrada






