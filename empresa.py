numHomens=int(input('quantidade de homens: '))
panetone=8.50
gastoHomens=float(panetone*numHomens)
numMulheres=int(input('quantidade de mulheres: '))
vinho=10
gastoMulheres=float(numMulheres*vinho)
gastomedio=(gastoHomens+gastoMulheres)/(numMulheres+numHomens)
total=gastoHomens+gastoMulheres
print('o valor total gasto pela empresa é de {} e o valor médio é de {} por pessoa'.format(total,gastomedio))